# LUVA Studio

<p align="center">
  <img src="img/luva-studio-logo.png" alt="LUVA Studio Logo" width="220" />
</p>

<p align="center">
  <strong>LUVA Studio</strong> is a passive offline analysis workspace for industrial control and SCADA packet captures.
  It reads capture files from disk only and turns them into a local dashboard with asset inventory, flow visibility,
  topology views, findings, and generated HTML reports.
</p>

---

## Overview

LUVA Studio is built for reviewing offline OT / ICS captures in a more polished desktop-friendly workflow.
Instead of starting from a raw command-line experience, you launch the local app, choose or upload a capture,
run analysis, and review the results from one interface.

The platform is designed around passive analysis only:

- no live sniffing
- no packet injection
- no interaction with the plant network
- no active scanning behavior

---

## Core capabilities

### Passive offline analysis

LUVA Studio processes:

- `.pcap`
- `.pcapng`
- `.gz`-wrapped capture files

It analyzes stored captures from disk and produces structured results for engineering, review, and investigation workflows.

### Asset discovery

LUVA Studio identifies endpoints and builds a usable view of the environment, including:

- IP and MAC visibility
- inferred device roles
- open ports
- protocol participation
- communication partners
- packet and byte context
- heuristic risk indicators

### Flow visibility

The platform builds communication views that help you inspect:

- source and destination relationships
- protocol usage
- packet counts
- byte counts
- ICS-related flow behavior

### Topology and communication mapping

LUVA Studio generates topology-oriented outputs that help visualize the environment:

- communication map HTML
- GraphML topology export
- embedded topology preview inside the local dashboard

### Findings and anomaly review

LUVA Studio surfaces findings for offline review through:

- findings tables in the GUI
- CSV exports
- HTML reporting
- protocol and traffic pattern summaries

### Reporting outputs

LUVA Studio can produce and display outputs such as:

- JSON analysis reports
- CSV exports
- HTML reports
- communication map HTML
- GraphML topology files

---

## Protocol coverage

LUVA Studio is designed to work with industrial traffic commonly found in OT and ICS environments.
Current built-in coverage includes support and visibility around protocols such as:

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
