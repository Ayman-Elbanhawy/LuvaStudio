from __future__ import annotations

import cgi
import csv
import json
import os
import shutil
import socket
import subprocess
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parent
REPORTS = ROOT / "reports"
LOG_DIR = ROOT / "artifacts" / "logs"
RUNNER = ROOT / "RunLuvaQuiet.py"
PYTHON = ROOT / ".venv" / "Scripts" / "python.exe"
WEB_DIR = ROOT / "webgui"
UPLOADS = ROOT / "uploads"
LAST_RUN_META = LOG_DIR / "last-run.json"
SERVER_META = LOG_DIR / "gui-server.json"


class LuvaHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def _send_json(self, payload: dict, status: int = 200) -> None:
        data = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path in {"/", "/index.html"}:
            self.path = "/webgui/index.html"
            return super().do_GET()
        if parsed.path == "/api/status":
            self._send_json(build_status())
            return
        if parsed.path == "/api/open-report":
            qs = parse_qs(parsed.query)
            target = qs.get("path", [""])[0]
            if not target:
                self._send_json({"ok": False, "error": "missing path"}, 400)
                return
            path = (ROOT / target).resolve() if not os.path.isabs(target) else Path(target).resolve()
            if not path.exists():
                self._send_json({"ok": False, "error": "file not found"}, 404)
                return
            os.startfile(str(path))
            self._send_json({"ok": True})
            return
        return super().do_GET()

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path == "/api/run":
            return self.handle_run()
        if parsed.path == "/api/upload":
            return self.handle_upload()
        self._send_json({"ok": False, "error": "not found"}, 404)

    def handle_upload(self) -> None:
        ctype, pdict = cgi.parse_header(self.headers.get("Content-Type", ""))
        if ctype != "multipart/form-data":
            self._send_json({"ok": False, "error": "expected multipart/form-data"}, 400)
            return
        pdict["boundary"] = pdict["boundary"].encode("utf-8")
        form = cgi.FieldStorage(fp=self.rfile, headers=self.headers, environ={"REQUEST_METHOD": "POST"}, keep_blank_values=True)
        file_item = form["file"] if "file" in form else None
        if not file_item or not getattr(file_item, "filename", None):
            self._send_json({"ok": False, "error": "missing file"}, 400)
            return

        UPLOADS.mkdir(parents=True, exist_ok=True)
        safe_name = Path(file_item.filename).name
        out_path = UPLOADS / safe_name
        with out_path.open("wb") as f:
            shutil.copyfileobj(file_item.file, f)
        self._send_json({"ok": True, "path": str(out_path)})

    def handle_run(self) -> None:
        length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(length)
        try:
            body = json.loads(raw.decode("utf-8"))
        except Exception:
            self._send_json({"ok": False, "error": "invalid json"}, 400)
            return

        capture = str(body.get("capture", "")).strip()
        if not capture:
            self._send_json({"ok": False, "error": "capture path required"}, 400)
            return

        capture_path = Path(capture)
        if not capture_path.exists():
            self._send_json({"ok": False, "error": "capture file not found"}, 404)
            return

        LOG_DIR.mkdir(parents=True, exist_ok=True)
        REPORTS.mkdir(parents=True, exist_ok=True)
        log_path = LOG_DIR / "gui-run.log"

        cmd = [str(PYTHON), str(RUNNER), str(capture_path), str(REPORTS)]
        proc = subprocess.run(cmd, capture_output=True, text=True, cwd=str(ROOT))
        log_path.write_text(
            "COMMAND: " + " ".join(cmd) + "\n\nSTDOUT:\n" + proc.stdout + "\n\nSTDERR:\n" + proc.stderr,
            encoding="utf-8",
        )

        last_run = {
            "ok": proc.returncode == 0,
            "exitCode": proc.returncode,
            "capture": str(capture_path),
            "log": str(log_path),
            "stdout": proc.stdout[-4000:],
            "stderr": proc.stderr[-4000:],
        }
        LAST_RUN_META.write_text(json.dumps(last_run, indent=2), encoding="utf-8")

        status = build_status()
        self._send_json(status, 200 if proc.returncode == 0 else 500)


def read_json(path: Path):
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def read_csv_rows(path: Path, limit: int = 200):
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    return rows[:limit]


def latest_file(pattern: str) -> Path | None:
    files = sorted(REPORTS.glob(pattern), key=lambda p: p.stat().st_mtime, reverse=True)
    return files[0] if files else None


def latest_html_report() -> Path | None:
    htmls = sorted(
        [p for p in REPORTS.glob("*.html") if "communication_map" not in p.name.lower()],
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )
    return htmls[0] if htmls else None


def latest_comm_map() -> Path | None:
    comm = REPORTS / "communication_map.html"
    if comm.exists():
        return comm
    return latest_file("*communication_map*.html")


def latest_topology() -> Path | None:
    topo = REPORTS / "topology.graphml"
    if topo.exists():
        return topo
    return latest_file("*.graphml")


def build_status() -> dict:
    analysis = read_json(REPORTS / "analysis_report.json")
    assets = read_csv_rows(REPORTS / "assets.csv")
    flows = read_csv_rows(REPORTS / "flows.csv")
    findings = read_csv_rows(REPORTS / "audit_findings.csv")
    html_report = latest_html_report()
    comm_map = latest_comm_map()
    topology = latest_topology()
    last_run = read_json(LAST_RUN_META)

    if last_run and isinstance(last_run.get("stdout"), str):
        for line in last_run["stdout"].splitlines():
            candidate = line.strip()
            if candidate.lower().endswith(".html") and "communication_map" not in candidate.lower():
                p = Path(candidate)
                if p.exists():
                    html_report = p
            elif candidate.lower().endswith(".graphml"):
                p = Path(candidate)
                if p.exists():
                    topology = p
            elif candidate.lower().endswith("communication_map.html"):
                p = Path(candidate)
                if p.exists():
                    comm_map = p

    return {
        "ok": True,
        "root": str(ROOT),
        "reportsDir": str(REPORTS),
        "sampleCaptures": [str(p) for p in sorted((ROOT / "public_pcaps").glob("*")) if p.is_file() and p.suffix.lower() in {".pcap", ".pcapng", ".gz"}],
        "uploads": [str(p) for p in sorted(UPLOADS.glob("*"), key=lambda p: p.stat().st_mtime, reverse=True)] if UPLOADS.exists() else [],
        "files": {
            "analysisJson": str(REPORTS / "analysis_report.json") if (REPORTS / "analysis_report.json").exists() else None,
            "htmlReport": str(html_report) if html_report else None,
            "commMap": str(comm_map) if comm_map else None,
            "topology": str(topology) if topology else None,
            "log": str(LOG_DIR / "gui-run.log") if (LOG_DIR / "gui-run.log").exists() else None,
        },
        "summary": analysis.get("summary") if analysis else None,
        "metadata": analysis.get("metadata") if analysis else None,
        "assets": analysis.get("assets", []) if analysis else assets,
        "flows": analysis.get("flows", []) if analysis else flows,
        "topology": analysis.get("topology") if analysis else None,
        "statistics": analysis.get("statistics") if analysis else None,
        "findings": findings,
        "lastRun": last_run,
    }


def find_open_port(host: str, start_port: int) -> int:
    port = start_port
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                sock.bind((host, port))
                return port
            except OSError:
                port += 1


def main() -> int:
    WEB_DIR.mkdir(parents=True, exist_ok=True)
    UPLOADS.mkdir(parents=True, exist_ok=True)
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    host = "127.0.0.1"
    requested_port = int(os.environ.get("LUVA_PORT", "8765"))
    port = find_open_port(host, requested_port)
    SERVER_META.write_text(json.dumps({"host": host, "port": port, "url": f"http://{host}:{port}"}, indent=2), encoding="utf-8")
    httpd = ThreadingHTTPServer((host, port), LuvaHandler)
    print(f"Luva Studio GUI running at http://{host}:{port}", flush=True)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
