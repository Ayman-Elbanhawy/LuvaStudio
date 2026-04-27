from pathlib import Path
import sys

from luva.cli.main import _analyze, _parse_mode, _parse_severity


def main() -> int:
    if len(sys.argv) < 3:
        print("Usage: RunLuvaQuiet.py <capture> <output_dir>")
        return 2

    capture = Path(sys.argv[1])
    output_dir = Path(sys.argv[2])

    _analyze(
        [capture],
        output_dir=output_dir,
        mode=_parse_mode("full"),
        min_severity=_parse_severity("INFO"),
        protocols=None,
        custom_rules_dir=None,
        anonymize_ips=False,
        mask_payload=False,
        export_graph=output_dir / "topology.graphml",
        show_progress=False,
        verbose=False,
        quiet=True,
        report_filename_suffix="",
        export_formats=("json", "csv", "html", "communication-map", "anomalies-ndjson"),
        chunk_size=0,
        compare_baseline=None,
        anomaly_subset_pcap=None,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
