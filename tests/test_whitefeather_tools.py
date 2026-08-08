from pathlib import Path

from wf_fingerprint_sync import merge
from wf_heatmap_export import build_html
from wf_propagation_manifest import build_manifest, load_dielectric
from wf_validate_survey import compare


def test_merge_two_files(tmp_path: Path) -> None:
    a = tmp_path / "a.csv"
    b = tmp_path / "b.csv"
    out = tmp_path / "merged.csv"
    a.write_text(
        "ts,bssid,ssid,channel,rssi,site_id\n2026-08-07T00:00:00Z,00:11:22:33:44:55,WF,11,-55,site-001\n",
        encoding="utf-8",
    )
    b.write_text(
        "ts,bssid,ssid,channel,rssi,site_id\n2026-08-07T00:01:00Z,00:11:22:33:44:55,WF,11,-57,site-001\n",
        encoding="utf-8",
    )
    merge([a, b], out)
    assert out.exists()
    assert out.read_text(encoding="utf-8").count("\n") == 3


def test_build_html(tmp_path: Path) -> None:
    report = [
        {
            "bssid": "00:11:22:33:44:55",
            "survey_mean": "-56",
            "sim": "-56",
            "error": "0",
            "pass": "True",
        }
    ]
    out = tmp_path / "report.html"
    build_html(report, "site-001", out)
    assert out.exists()
    assert "site-001" in out.read_text(encoding="utf-8")


def test_build_manifest(tmp_path: Path) -> None:
    dielectric = tmp_path / "dielectric.json"
    dielectric.write_text(
        '{"concrete":{"2.4GHz":4,"5GHz":3.8},"brick":{"2.4GHz":3.5,"5GHz":3.4}}',
        encoding="utf-8",
    )
    data = load_dielectric(dielectric)
    manifest = build_manifest(
        "site-001", ["concrete", "brick"], ["2.4GHz", "5GHz"], data
    )
    assert manifest["materials"]["concrete"]["5GHz"] == 3.8
    assert manifest["site_id"] == "site-001"


def test_compare_passes_within_threshold() -> None:
    survey = {"00:11:22:33:44:55": [-56.0, -54.0, -57.0]}
    sim = {"00:11:22:33:44:55": -56.0}
    report = compare(survey, sim, 3.0)
    assert report[0]["pass"] is True


def test_compare_fails_outside_threshold() -> None:
    survey = {"00:11:22:33:44:55": [-40.0]}
    sim = {"00:11:22:33:44:55": -56.0}
    report = compare(survey, sim, 3.0)
    assert report[0]["pass"] is False
