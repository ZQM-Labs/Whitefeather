"""WhiteFeather heatmap renderer stub.

Converts validation report + site config into an HTML heatmap viewer.
Intended backend: wifi-heatmapper or wifi-3d-fusion exporter.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


def load_report(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def build_html(report: list[dict], site_id: str, out: Path) -> None:
    rows = "\n".join(
        f"<tr><td>{r['bssid']}</td><td>{r.get('survey_mean', '')}</td><td>{r.get('sim', '')}</td><td>{r.get('error', '')}</td><td>{r.get('pass', '')}</td></tr>"
        for r in report
    )
    html = f"""<!doctype html>
<meta charset="utf-8">
<title>{site_id} — validation report</title>
<style>
body {{ font-family: system-ui; margin: 2rem; }}
table {{ border-collapse: collapse; width: 100%; }}
th, td {{ border: 1px solid #ccc; padding: 0.5rem; }}
.pass {{ background: #cfc; }} .fail {{ background: #fcc; }}
</style>
<h1>{site_id} validation report</h1>
<table>
<thead><tr><th>bssid</th><th>survey_mean</th><th>sim</th><th>error</th><th>pass</th></tr></thead>
<tbody>{rows}</tbody>
</table>
"""
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(f"heatmap report written: {out}")


def main() -> int:
    ap = argparse.ArgumentParser(description="WhiteFeather validation HTML exporter")
    ap.add_argument("--report", type=Path, required=True)
    ap.add_argument("--site-id", required=True)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    build_html(load_report(args.report), args.site_id, args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
