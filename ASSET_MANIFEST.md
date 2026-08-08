# WhiteFeather Authorized Asset Manifest
Generated: 2026-08-07
Scope: global observability platform across all open data sources — property Wi-Fi SLAM + RF propagation + digital twin, not limited to a single property.
EaglesNest is the close upstream capability source; integration is intentional and tightly coupled.

## Direction 1 — Wi-Fi SLAM / CSI tomography
| Asset | Path | Purpose |
|---|---|---|
| linux-80211n-csitool | `02_geometry/csi-capture/linux-80211n-csitool` | Intel 5300 802.11n CSI acquisition |
| nexmon_csi | `02_geometry/csi-capture/nexmon_csi` | Broadcom/Cypress CSI extraction (a/g/n/ac) |

## Direction 2 — RF propagation / 3D digital twin mapping
| Asset | Path | Purpose |
|---|---|---|
| wifi-3d-fusion | `04_simulation/propagation/wifi-3d-fusion` | Wi-Fi CSI + RSSI 3D spatial awareness |
| wifi-rssi-indoor dataset | `03_fingerprints/rssi-datasets/wifi-rssi-indoor` | Indoor Wi-Fi fingerprint corpus |
| pylayers | `04_simulation/propagation/pylayers` | Site-specific radio propagation simulator |
| wifi-survey-heatmap | `01_floorplans/survey/tools/wifi-survey-heatmap` | Survey data heatmap overlay |
| wifi-heatmapper | `06_exports/heatmap-viz/tools/wifi-heatmapper` | Heatmap visualization |

## Material/dielectric reference
- `04_simulation/propagation/materials/dielectric-reference.json` — global material library at 2.4/5/6 GHz.

## Additions table — global observability leads
| Repo / Dataset | Alignment | Notes |
|---|---|---|
| `nvlabs/diff-rt` / `TWIST-Lab/RF-Vision` | Direction 2 | Sionna differentiability + Blender scene pipeline |
| `nesl/WiFislam` | Direction 1 | Android Wi-Fi SLAM workflow |
| `wifi-survey-heatmap` | survey viz | already cloned |
| `chrieke/awesome-satellite-imagery-datasets` | IMINT ref | exterior/rooftop/antenna context |
| `VincentDary/open-firmware-dataset-builder` | TECHINT ref | firmware dataset builder |
| `facebookresearch/real-acoustic-fields` | ACINT ref | room acoustics dataset |

## Policy
- Global use permitted. Cross-project linkage to EaglesNest and Daly is expected.
- Cloud telemetry allowed for propagation modeling and dataset augmentation.
- Observability chain: every export under `06_exports/` must carry source hash + timestamp + site ID.
