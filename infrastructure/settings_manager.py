
import json
from pathlib import Path


class SettingsManager:
    """Управляет настройками приложения."""

    SETTINGS_FILE = Path(__file__).resolve().parent.parent / "settings.json"

    DEFAULT_SETTINGS = {
        "window_width": 900,
        "window_height": 650
    }

    def load_settings(self):
        """Загружает настройки из файла."""

        if not self.SETTINGS_FILE.exists():
            return self.DEFAULT_SETTINGS.copy()

        try:
            with self.SETTINGS_FILE.open("r", encoding="utf-8") as file:
                settings = json.load(file)

            width = int(settings.get("window_width", 900))
            height = int(settings.get("window_height", 650))

            return {
                "window_width": max(750, min(width, 1600)),
                "window_height": max(550, min(height, 1200))
            }

        except (OSError, ValueError, TypeError, json.JSONDecodeError):
            return self.DEFAULT_SETTINGS.copy()

    def save_settings(self, settings):
        """Сохраняет настройки в файл."""

        try:
            with self.SETTINGS_FILE.open("w", encoding="utf-8") as file:
                json.dump(settings, file, indent=4)

        except OSError as error:
            print(f"Не удалось сохранить настройки: {error}")
