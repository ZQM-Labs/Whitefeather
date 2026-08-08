"""WhiteFeather simulation validator.

Compares survey fingerprint RSSI means against simulation outputs and emits a
validation report with error thresholds.
"""

from __future__ import annotations

import argparse
import csv
import statistics
from pathlib import Path


def load_survey(path: Path) -> dict[str, list[float]]:
    by_bssid: dict[str, list[float]] = {}
    with path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            bssid = row.get("bssid", "").strip()
            rssi = row.get("rssi", "").strip()
            if not bssid or not rssi:
                continue
            by_bssid.setdefault(bssid, []).append(float(rssi))
    return by_bssid


def load_sim(path: Path) -> dict[str, float]:
    out: dict[str, float] = {}
    with path.open("r", encoding="utf-8") as f:
        it = iter(f)
        for line in it:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            bssid, rssi = line.split(",", 1)
            out[bssid.strip()] = float(rssi.strip())
    return out


def compare(
    survey: dict[str, list[float]], sim: dict[str, float], threshold: float
) -> list[dict]:
    report = []
    for bssid, sim_rssi in sim.items():
        vals = survey.get(bssid)
        if not vals:
            report.append(
                {
                    "bssid": bssid,
                    "survey_mean": None,
                    "sim": sim_rssi,
                    "error": None,
                    "pass": False,
                }
            )
            continue
        mean = statistics.mean(vals)
        error = abs(mean - sim_rssi)
        report.append(
            {
                "bssid": bssid,
                "survey_mean": mean,
                "sim": sim_rssi,
                "error": error,
                "pass": error <= threshold,
            }
        )
    return report


def write_report(report: list[dict], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=["bssid", "survey_mean", "sim", "error", "pass"]
        )
        writer.writeheader()
        writer.writerows(report)


def main() -> int:
    ap = argparse.ArgumentParser(
        description="WhiteFeather survey-vs-simulation validator"
    )
    ap.add_argument(
        "--survey",
        type=Path,
        required=True,
        help="merged fingerprint CSV from wf_fingerprint_sync.py",
    )
    ap.add_argument(
        "--sim", type=Path, required=True, help="simulation RSSI CSV: bssid,rssi"
    )
    ap.add_argument(
        "--threshold", type=float, default=3.0, help="max acceptable RSSI error dB"
    )
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()

    survey = load_survey(args.survey)
    sim = load_sim(args.sim)
    report = compare(survey, sim, args.threshold)
    write_report(report, args.out)
    failed = sum(1 for r in report if not r["pass"])
    print(
        f"validated {len(report)} APs, {failed} failures, threshold={args.threshold} dB"
    )
    return 0 if failed == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
