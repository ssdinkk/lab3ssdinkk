
from infrastructure.settings_manager import SettingsManager


manager = SettingsManager()

settings = manager.load_settings()

print("Ширина окна:", settings["window_width"])
print("Высота окна:", settings["window_height"])

manager.save_settings({
    "window_width": 1000,
    "window_height": 700
})

print("Настройки сохранены!")
