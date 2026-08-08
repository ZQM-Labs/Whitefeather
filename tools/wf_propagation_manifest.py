"""WhiteFeather propagation model applier.

Applies material/dielectric parameters from dielectric-reference.json to a site config
and emits a propagation-ready manifest for wifi-3d-fusion or pylayers.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import UTC, datetime
from pathlib import Path

DEFAULT_DIELECTRIC = Path(
    "04_simulation/propagation/materials/dielectric-reference.json"
)


def load_dielectric(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"dielectric reference missing: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def build_manifest(
    site_id: str, materials: list[str], bands: list[str], dielectric: dict
) -> dict:
    materials_out: dict[str, dict[str, object]] = {}
    for mat in materials:
        entry = dielectric.get(mat, {})
        materials_out[mat] = {str(b): entry.get(b) for b in bands}
    return {
        "site_id": site_id,
        "generated": datetime.now(UTC).isoformat(),
        "bands": bands,
        "materials": materials_out,
    }


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser(
        description="WhiteFeather propagation manifest builder"
    )
    ap.add_argument("--site-id", required=True, help="site identifier, e.g. site-001")
    ap.add_argument(
        "--materials",
        nargs="+",
        required=True,
        help="material keys from dielectric-reference.json",
    )
    ap.add_argument("--bands", nargs="+", default=["2.4GHz", "5GHz", "6GHz"])
    ap.add_argument("--dielectric", type=Path, default=DEFAULT_DIELECTRIC)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()

    dielectric = load_dielectric(args.dielectric)
    manifest = build_manifest(args.site_id, args.materials, args.bands, dielectric)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    print(f"manifest written: {args.out}")
    print(f"source hash: {sha256_of(args.dielectric)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
