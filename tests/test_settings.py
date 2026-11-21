
import unittest
import tempfile
import json
from pathlib import Path

from infrastructure.settings_manager import SettingsManager


class TestSettingsManager(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.settings_file = (
            Path(self.temp_dir.name) / "settings.json"
        )

        self.manager = SettingsManager()
        self.manager.SETTINGS_FILE = self.settings_file

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_load_default_settings(self):
        settings = self.manager.load_settings()

        self.assertEqual(settings["window_width"], 900)
        self.assertEqual(settings["window_height"], 650)

    def test_save_settings(self):
        settings = {
            "window_width": 1000,
            "window_height": 700
        }

        self.manager.save_settings(settings)

        with open(
            self.settings_file,
            "r",
            encoding="utf-8"
        ) as file:
            saved_settings = json.load(file)

        self.assertEqual(saved_settings, settings)

    def test_load_saved_settings(self):
        settings = {
            "window_width": 1100,
            "window_height": 750
        }

        self.manager.save_settings(settings)
        loaded_settings = self.manager.load_settings()

        self.assertEqual(loaded_settings, settings)


if __name__ == "__main__":
    unittest.main()
