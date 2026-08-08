# Whitefeather

WiFi survey/simulation validation toolchain.

## CLI tools

`tools/wf_fingerprint_sync.py`
- Merge site-scoped survey CSVs into one corpus manifest under `03_fingerprints`.
- Input columns: timestamp, bssid, ssid, channel, rssi, site_id.
- Outputs CSV with `source_file` + `source_hash` for provenance.

`tools/wf_validate_survey.py`
- Compare survey RSSI means against simulation RSSI outputs.
- Emits validation report: bssid, survey_mean, sim, error, pass/fail.
- Exit 0 if all pass; exit 2 if failures exceed threshold.

`tools/wf_propagation_manifest.py`
- Load dielectric material parameters from `dielectric-reference.json`.
- Emit propagation-ready manifest keyed by material + band.

`tools/wf_heatmap_export.py`
- Render validation report as HTML table for quick review.

## Usage

```bash
python tools/wf_fingerprint_sync.py --out 03_fingerprints/corpus.csv survey_a.csv survey_b.csv
python tools/wf_validate_survey.py --survey 03_fingerprints/corpus.csv --sim simulation.csv --threshold 3.0 --out report.csv
python tools/wf_propagation_manifest.py --site-id site-001 --materials concrete brick --out manifest.json
python tools/wf_heatmap_export.py --report report.csv --site-id site-001 --out report.html
```

## Verify

```bash
make ci
```

## Integration: zqm-intel-platforms
This repo vendors `zqm-intel-platforms>=0.1.0` as a dependency. Use the shared SIEM/OSINT/CTI wrappers for Splunk HEC, Loki, and Windows-telemetry export defined in that package.
