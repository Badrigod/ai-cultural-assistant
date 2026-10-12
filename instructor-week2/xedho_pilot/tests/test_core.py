import tempfile
import unittest
from pathlib import Path
from core import answer, approved_passages, event_counts, log_event, load_artifact


class PilotTests(unittest.TestCase):
    def test_draft_refuses_answers(self):
        r = load_artifact()
        response, source = answer("What is its traditional use?", r)
        self.assertIsNone(source)
        self.assertIn("not available", response)

    def test_approved_passage_requires_approved_source(self):
        r = load_artifact()
        r["status"] = "approved"
        r["approval"]["reviewer"] = "Museum reviewer"
        r["approval"]["date"] = "2026-09-28"
        r["inventory_row"] = 1
        r["image"]["permission"] = "confirmed"
        r["traditional_use"] = "Test use"
        r["story_en"] = "Test story"
        r["story_so"] = "Sheeko tijaabo"
        r["sources"] = [{"id": "S1", "approved": True}]
        r["passages"] = [{"source_id": "S1", "language": "en", "approved": True, "text": "Test material: woven fibres."},
                         {"source_id": "S1", "language": "so", "approved": True, "text": "Qoraal tijaabo ah."}]
        self.assertEqual(answer("woven fibres", r), ("Test material: woven fibres.", "S1"))
        r["sources"][0]["approved"] = False
        self.assertEqual(approved_passages(r), [])

    def test_event_log_is_aggregate_only(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "events.db"
            log_event("page_view", path=path)
            log_event("page_view", path=path)
            self.assertEqual(event_counts(path), [("KHH-005", "page_view", 2)])


if __name__ == "__main__":
    unittest.main()

