
import tkinter as tk

from infrastructure.settings_manager import SettingsManager
from presentation.settings_frame import SettingsFrame
from presentation.rules_frame import RulesFrame
from application.game_service import GameService
from presentation.game_frame import GameFrame

class MainWindow:
    """Главное окно приложения Морской бой."""

    def __init__(self, root):
        self.root = root
        self.settings_manager = SettingsManager()

        settings = self.settings_manager.load_settings()

        self.root.title("Морской бой")
        self.root.geometry(
            f"{settings['window_width']}x{settings['window_height']}"
        )
        self.root.minsize(750, 550)
        self.root.configure(bg="#F5F7FA")

        self.create_menu()

    def create_menu(self):
        """Создаёт главное меню приложения."""

        for widget in self.root.winfo_children():
            widget.destroy()

        title = tk.Label(
            self.root,
            text="Морской бой",
            font=("Segoe UI", 30, "bold"),
            bg="#F5F7FA",
            fg="#244B73"
        )
        title.pack(pady=(100, 15))

        subtitle = tk.Label(
            self.root,
            text="Классическая морская стратегия",
            font=("Segoe UI", 13),
            bg="#F5F7FA",
            fg="#64748B"
        )
        subtitle.pack(pady=10)

        new_game_button = tk.Button(
            self.root,
            text="Новая игра",
            font=("Segoe UI", 13),
            width=20,
            height=2,
            command=self.start_game
        )
        new_game_button.pack(pady=12)

        settings_button = tk.Button(
            self.root,
            text="Настройки",
            font=("Segoe UI", 13),
            width=20,
            height=2,
            command=self.open_settings
        )
        settings_button.pack(pady=12)

        rules_button = tk.Button(
            self.root,
            text="Правила игры",
            font=("Segoe UI", 13),
            width=20,
            height=2,
            command=self.open_rules
        )
        rules_button.pack(pady=12)

        exit_button = tk.Button(
            self.root,
            text="Выход",
            font=("Segoe UI", 13),
            width=20,
            height=2,
            command=self.root.destroy
        )
        exit_button.pack(pady=12)

    def open_settings(self):
        """Открывает экран настроек."""

        for widget in self.root.winfo_children():
            widget.destroy()

        SettingsFrame(
            self.root,
            self.settings_manager,
            self.show_main_menu
        )

    def show_main_menu(self):
        """Возвращает пользователя в главное меню."""

        self.create_menu()

    def open_rules(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        RulesFrame(self.root, self.show_main_menu)

    def start_game(self):
        self.game_service = GameService()
        self.game_service.start_new_game()

        for widget in self.root.winfo_children():
            widget.destroy()

        GameFrame(
            self.root,
            self.game_service,
            self.show_main_menu
        )