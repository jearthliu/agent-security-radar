from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "validate_catalog.py"
SPEC = importlib.util.spec_from_file_location("validate_catalog", MODULE_PATH)
assert SPEC and SPEC.loader
validate_catalog = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validate_catalog)


class CatalogValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.payload = json.loads(
            (ROOT / "data" / "papers.json").read_text(encoding="utf-8")
        )

    def validate_payload(self, payload: dict) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "papers.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            validate_catalog.validate(path)

    def test_current_catalog_is_valid(self) -> None:
        self.validate_payload(self.payload)

    def test_rejects_report_date_outside_research_window(self) -> None:
        payload = copy.deepcopy(self.payload)
        payload["report_date"] = "2026-07-27"

        with self.assertRaisesRegex(
            ValueError, "report_date must fall within the research window"
        ):
            self.validate_payload(payload)

    def test_rejects_unknown_lifecycle_stage(self) -> None:
        payload = copy.deepcopy(self.payload)
        payload["papers"][0]["lifecycle_stages"] = ["unbounded-authority"]

        with self.assertRaisesRegex(ValueError, "unsupported lifecycle stage"):
            self.validate_payload(payload)


if __name__ == "__main__":
    unittest.main()
