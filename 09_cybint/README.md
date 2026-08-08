# CYBINT / CYBERINT — Cyber Intelligence

Definition: Intelligence gathered from cyberspace, focusing on infrastructure, threat actors, malware, and digital vulnerabilities.

Core Sources:
- Network telemetry, honeypots, malware reverse-engineering, dark web monitoring, incident response logs.

Primary Applications:
- Attribution of cyberattacks, threat hunting, vulnerability management, and defense of critical digital infrastructure.

Property mapping relevance:
- Router/AP telemetry from any site in the global observability platform is valid input.
- Honeypot/telemetry tooling is relevant when monitoring edge infrastructure across sites.
- Vulnerability scans of AP firmware and router SSIDs are standard maintenance input.

Local notes:
- Telemetry exports go to `09_cybint/` with site ID + timestamp + checksum.
- External mesh/presence scanning protocols from SIGINT are permissible when aligned with global observability policy.
- Do not ingest third-party telemetry without provenance header.
