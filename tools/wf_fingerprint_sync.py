"""WhiteFeather fingerprint synchronizer.

Merge RSSI/BSSID survey CSVs into a single corpus manifest under 03_fingerprints.
Inputs are site-scoped CSVs with columns: timestamp, bssid, ssid, channel, rssi, site_id.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
from pathlib import Path


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def merge(csv_paths: list[Path], out: Path) -> int:
    rows = 0
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8", newline="") as dst:
        writer = csv.writer(dst)
        writer.writerow(
            [
                "timestamp",
                "bssid",
                "ssid",
                "channel",
                "rssi",
                "site_id",
                "source_file",
                "source_hash",
            ]
        )
        for p in csv_paths:
            source_hash = sha256_of(p)
            with p.open("r", encoding="utf-8") as src:
                reader = csv.DictReader(src)
                for row in reader:
                    writer.writerow(
                        [
                            row.get("timestamp", ""),
                            row.get("bssid", ""),
                            row.get("ssid", ""),
                            row.get("channel", ""),
                            row.get("rssi", ""),
                            row.get("site_id", ""),
                            p.name,
                            source_hash,
                        ]
                    )
                    rows += 1
    print(f"merged {rows} rows from {len(csv_paths)} files -> {out}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="WhiteFeather fingerprint corpus builder")
    ap.add_argument("inputs", nargs="+", type=Path, help="input survey CSVs")
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    missing = [p for p in args.inputs if not p.exists()]
    if missing:
        raise SystemExit(f"missing inputs: {missing}")
    return merge(args.inputs, args.out)


if __name__ == "__main__":
    raise SystemExit(main())
