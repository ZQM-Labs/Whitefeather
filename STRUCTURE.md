# WhiteFeather Structure

Global property-scale radio observability arm across all open data sources — not limited to a single property.
Cross-project index: `C:\Users\zqmco\INT_TOOLKIT_INDEX.md`

00_eaglesnest_mirror/ — Hash-verified capability sync from `EaglesNest` (upstream; keep aligned)
01_floorplans/ — Source drawings, PDFs, scans, BIM exports, global site templates
02_geometry/ — Point clouds, meshes, room/floor models; multi-site reuse
03_fingerprints/ — RSSI/BSSID survey data; global radio-map corpus
04_simulation/ — Ray tracer configs, AP placements, material metadata; cross-site propagation models
05_validation/ — Survey vs simulation, error logs, checksums; global benchmark thresholds
06_exports/ — Final renders, heatmaps, immersive viewers; public delivery formats
07_humint/ — Observer notes, behavior references; anonymized/cross-site
08_masint/ — Acoustic, thermal, radar/UWB signature references; global sensor context
09_cybint/ — Network telemetry, audit notes; local + remote AP/router telemetry, no hard local-only block
09_techint/ — AP/firmware datasheets, antenna specs; global hardware taxonomy
09_temp_scratch/ — Scratch artifacts; ephemeral, not retained in final
10_finint/ — Procurement tracking across sites
11_techint/ — AP/firmware datasheets, antenna specs; global reference
12_final/ — Signed-off deliverables and hashes; global release channel
13_medint_bioint/ — Medical/biological references; environmental/health crossover
14_imint/ — Imagery for exterior/roof/antenna context; global satellite/aerial feeds
15_acint/ — Acoustic diagnostics; room + outdoor signatures
16_radint/ — Local RF interference diagnostics; global spectrum monitoring
17_socint/ — Social-media public context; crowd-sourced coverage signals
18_geofinint/ — Financial/geospatial linkage; site ROI / infrastructure investment mapping

## Pipeline
01 → 02/03 → 04 → 05 → 06 with 16_radint + 09_cybint as live telemetry inputs.
00_eaglesnest_mirror is upstream capability source, not isolated mirror.
