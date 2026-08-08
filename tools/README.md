# WhiteFeather Tools

Location: `tools/`

wf_fingerprint_sync.py
  Merge site-scoped survey CSVs into one corpus manifest under 03_fingerprints/.

wf_propagation_manifest.py
  Apply dielectric/materials parameters from a reference JSON to a site and emit a
  propagation-ready manifest for pylayers / wifi-3d-fusion.

wf_validate_survey.py
  Compare survey fingerprint means against simulation outputs.
  Emits CSV report with dB error and pass/fail flags.

wf_heatmap_export.py
  Convert a validation report + site config into an HTML viewer.

Verified: 2026-08-07 — 5/5 tests passing.
