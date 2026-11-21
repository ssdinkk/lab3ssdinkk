
import tkinter as tk

from infrastructure.settings_manager import SettingsManager
from application.game_service import GameService
from presentation.settings_frame import SettingsFrame
from presentation.rules_frame import RulesFrame
from presentation.game_frame import GameFrame
from presentation.placement_frame import PlacementFrame


class MainWindow:
    """Главное окно приложения Морской бой."""

    def __init__(self, root):
        self.root = root
        self.settings_manager = SettingsManager()
        self.game_service = None

        settings = self.settings_manager.load_settings()

        self.root.title("Морской бой")
        self.root.geometry(
            f"{settings['window_width']}x{settings['window_height']}"
        )
        self.root.minsize(750, 550)
        self.root.configure(bg="#F5F7FA")

        self.create_menu()

    def create_menu(self):
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

        tk.Button(
            self.root,
            text="Новая игра",
            font=("Segoe UI", 13),
            width=20,
            height=2,
            command=self.start_game
        ).pack(pady=12)

        tk.Button(
            self.root,
            text="Настройки",
            font=("Segoe UI", 13),
            width=20,
            height=2,
            command=self.open_settings
        ).pack(pady=12)

        tk.Button(
            self.root,
            text="Правила игры",
            font=("Segoe UI", 13),
            width=20,
            height=2,
            command=self.open_rules
        ).pack(pady=12)

        tk.Button(
            self.root,
            text="Выход",
            font=("Segoe UI", 13),
            width=20,
            height=2,
            command=self.root.destroy
        ).pack(pady=12)

    def start_game(self):
        self.game_service = GameService()
        self.game_service.start_new_game()

        for widget in self.root.winfo_children():
            widget.destroy()

        PlacementFrame(
            self.root,
            self.game_service,
            self.open_game,
            self.show_main_menu
        )

    def open_game(self):
        GameFrame(
            self.root,
            self.game_service,
            self.show_main_menu
        )

    def open_settings(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        SettingsFrame(
            self.root,
            self.settings_manager,
            self.show_main_menu
        )

    def open_rules(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        RulesFrame(
            self.root,
            self.show_main_menu
        )

    def show_main_menu(self):
        self.create_menu()
