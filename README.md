# LUVA Studio

<p align="center">
  <img src="img/luva-studio-logo.png" alt="LUVA Studio Logo" width="220" />
</p>

<p align="center">
  <strong>LUVA Studio</strong> is a premium local workspace for passive OT / ICS packet analysis — turning stored captures into asset intelligence, flow visibility, topology context, findings, and polished HTML reporting from one desktop-friendly dashboard.
</p>

<p align="center">
  Built for offline review. Designed for control-room clarity. Focused on passive analysis only.
</p>

---

## Why LUVA Studio

LUVA Studio is built for engineers, analysts, and reviewers who want a more polished way to inspect industrial packet captures without losing technical depth.

Instead of working through scattered outputs first, LUVA Studio gives you a guided local workflow:

- launch the app
- open the browser dashboard
- choose or upload a capture
- run passive analysis
- review assets, flows, topology, findings, and reports in one place

This makes LUVA Studio feel closer to a purpose-built OT analysis workstation than a raw parser front end.

---

## Built for passive offline analysis

LUVA Studio works with stored capture files from disk, including:

- `.pcap`
- `.pcapng`
- `.gz`-wrapped captures

The platform is intentionally focused on passive workflows:

- no live sniffing
- no packet injection
- no active scanning behavior
- no interaction with the plant network

That makes it well suited for offline review, engineering validation, packet-driven investigation, and presentation-ready reporting.

---

## What you get in the experience

### A premium local OT dashboard

LUVA Studio wraps the underlying analysis workflow in a polished browser-based control surface with:

- launch-and-run simplicity
- mission-control style analysis flow
- operational summary cards
- protocol visibility badges
- embedded report viewing
- built-in help and guided review

### Asset intelligence

LUVA Studio helps transform raw packet data into a clearer inventory view of the environment, including:

- IP and MAC visibility
- inferred roles
- open ports
- protocol participation
- communication partners
- packet and byte context
- heuristic risk indicators

### Flow and communication visibility

Traffic is organized into readable communication views that help you inspect:

- source-to-destination relationships
- protocol usage across systems
- packet counts and byte volume
- ICS-related communication behavior

### Topology and mapping context

LUVA Studio supports broader environment understanding through:

- communication map HTML output
- GraphML topology export
- embedded topology review in the local dashboard

### Findings and report-ready outputs

The platform supports review and presentation workflows with outputs such as:

- findings tables inside the GUI
- JSON analysis reports
- CSV exports
- HTML reports
- communication map output
- GraphML topology files

---

## Protocol coverage

LUVA Studio is designed for industrial traffic visibility across common OT / ICS environments. Current built-in coverage includes support and analysis around:

- Modbus/TCP
- S7comm
- DNP3
- OPC UA
- EtherNet/IP
- IEC 60870-5-104
- BACnet/IP
- MQTT
- SNMP
- Omron FINS
- GE SRTP

---

## LUVA Studio workflow

1. Launch `StartMe.bat`
2. The launcher checks Python and prepares the local environment
3. The LUVA Studio GUI opens in the browser
4. Choose a bundled sample capture or upload your own file
5. Click **Run Luva**
6. Review results in the tabs:
   - Overview
   - Assets
   - Flows
   - Topology
   - Findings
   - Report

---

## Product showcase

LUVA Studio is designed to feel like a complete local OT analysis workstation rather than a simple packet viewer. The screenshots below highlight the main operating views and how the workflow moves from capture selection to investigation and reporting.

### Control-room dashboard experience

The main dashboard brings together launch controls, operational summary cards, system status, protocol visibility, and direct navigation into every major analysis surface.

<p align="center">
  <img src="img/MainPageScreenshot.png" alt="LUVA Studio main dashboard" width="1000" />
</p>

<p align="center">
  <img src="img/main.png" alt="LUVA Studio alternate dashboard view" width="1000" />
</p>

### Guided analysis workflow

#### Overview

Start with the Overview tab to get the capture context, protocol visibility, timestamps, runtime information, and quick operational understanding of the loaded analysis.

<p align="center">
  <img src="img/MainPageScreenshot_OverviewTab.png" alt="LUVA Studio overview tab" width="1000" />
</p>

#### Assets

Move into the Assets tab to inspect discovered endpoints, inferred roles, protocol participation, open ports, and risk-oriented visibility in a clean inventory-style layout.

<p align="center">
  <img src="img/MainPageScreenshot_AssetsTab.png" alt="LUVA Studio assets tab" width="1000" />
</p>

#### Flows

Use the Flows tab to review communication relationships, traffic volume, and protocol-linked activity between systems across the analyzed capture set.

<p align="center">
  <img src="img/MainPageScreenshot_FlowsTab.png" alt="LUVA Studio flows tab" width="1000" />
</p>

#### Topology

The Topology tab helps turn raw traffic into a more understandable environment view, with communication mapping and topology-oriented outputs for deeper review.

<p align="center">
  <img src="img/MainPageScreenshot_TopologyTab.png" alt="LUVA Studio topology tab" width="1000" />
</p>

#### Findings

The Findings tab is built for quick review of surfaced issues, anomalies, and investigation signals so you can move faster from analysis to assessment.

<p align="center">
  <img src="img/MainPageScreenshot_FindingsTab.png" alt="LUVA Studio findings tab" width="1000" />
</p>

#### Report

When you want a polished deliverable, the Report tab embeds the latest generated HTML report directly inside the application for a presentation-friendly review experience.

<p align="center">
  <img src="img/MainPageScreenshot_ReportTab.png" alt="LUVA Studio report tab" width="1000" />
</p>

### What this showcase demonstrates

- a premium local OT / ICS dashboard experience
- passive offline packet analysis workflows
- asset and flow visibility from one interface
- topology and findings review without leaving the app
- report-ready output for investigation and presentation use

---

## Typical output files

A completed run can generate files such as:

- `reports\analysis_report.json`
- `reports\assets.csv`
- `reports\flows.csv`
- `reports\audit_findings.csv`
- `reports\communication_map.html`
- `reports\topology.graphml`
- capture-specific HTML report files

---

## Repository layout

- `StartMe.bat` — Windows launcher
- `LuvaGuiServer.py` — local GUI web server
- `RunLuvaQuiet.py` — quiet analysis runner used by the GUI
- `webgui/` — local browser interface and help page
- `luva/` — analysis engine code
- `ot_baseline/` — baseline analysis components
- `public_pcaps/` — sample capture files
- `reports/` — generated outputs
- `img/` — logos and current LUVA Studio screenshots
- `artifacts/` — local helper outputs and logs

---

## Notes

- LUVA Studio is intended for local desktop use
- analysis is passive and file-based
- the GUI is designed to make OT / ICS capture review easier for offline workflows
- the built-in Help page is available from inside the GUI

---

## Project information

GitHub: github.com/Ayman-Elbanhawy/LuvaStudioio  
Website: [SoftwareMile.com](https://SoftwareMile.com)  
Support: Github@Softwaremile.com
