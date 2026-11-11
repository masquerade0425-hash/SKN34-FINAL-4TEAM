"""Focused data contract tests; no database, network or application startup."""
import hashlib
import json
import unittest
from unittest.mock import patch
import build_traditions as catalog


class TraditionCatalogTest(unittest.TestCase):
    def setUp(self):
        self.current = catalog.read(catalog.RESOURCES / "genre-templates.json")

    def test_original_eleven_are_unchanged_in_current_and_frozen_resources(self):
        expected = "333e2e2f970881ab2533312ec5c523e74f70cccf0c1f33bc356b274c22c538b8"
        for name in ("genre-templates.json", "genre-templates-v1.json"):
            records = catalog.read(catalog.RESOURCES / name)[:11]
            digest = hashlib.sha256(json.dumps(records, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
            self.assertEqual(expected, digest, name)
        self.assertEqual(list(catalog.LEGACY), [t["genre"] for t in catalog.read(catalog.RESOURCES / "genre-templates-v1.json")])

    def test_runtime_catalog_is_reproducible_and_includes_all_fifteen_traditions(self):
        self.assertEqual(self.current, catalog.build(self.current))
        self.assertEqual(list(catalog.LEGACY + catalog.TRADITIONS), [t["genre"] for t in self.current])
        self.assertEqual(catalog.build(self.current), catalog.build(catalog.build(self.current)))

    def test_source_documents_match_cards_without_creative_scaffold(self):
        for genre in catalog.TRADITIONS:
            directory = catalog.ROOT / genre / "source"
            data = catalog.read(directory / "tradition-cards.json")
            template = catalog.read(directory / "template.json")
            self.assertNotIn("basic_template", template, genre)
            self.assertEqual(template["content_markdown"], (directory / "original.md").read_text(encoding="utf-8-sig"), genre)
            sections = template["setting_bible"]["sections"]
            self.assertEqual(len(data["cards"]), len(sections), genre)
            for card, section in zip(data["cards"], sections):
                self.assertEqual(card["title"], section["title"], genre)
                self.assertEqual(card["body"], section["content_markdown"], genre)
                self.assertEqual(card["cardType"], section["card_type"], genre)
                self.assertNotIn("도입 예시", section["template_part"], genre)
            self.assertTrue(data["sources"], genre)

    def test_bad_card_type_and_duplicate_keys_are_rejected(self):
        real_read = catalog.read
        for mutation in ("type", "duplicate"):
            def modified(path):
                data = real_read(path)
                if path.name == "tradition-cards.json":
                    if mutation == "type":
                        data["cards"][0]["cardType"] = "unsupported"
                    else:
                        data["cards"].append(data["cards"][0])
                return data
            with patch.object(catalog, "read", side_effect=modified):
                with self.assertRaises(AssertionError):
                    catalog.build(self.current)


if __name__ == "__main__":
    unittest.main()
