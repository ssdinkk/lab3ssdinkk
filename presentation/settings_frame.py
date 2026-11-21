
import tkinter as tk
from tkinter import messagebox


class SettingsFrame:
    """Экран настроек приложения."""

    def __init__(self, root, settings_manager, on_back):
        self.root = root
        self.settings_manager = settings_manager
        self.on_back = on_back

        self.frame = tk.Frame(root, bg="#F5F7FA")
        self.frame.pack(fill="both", expand=True)

        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(
            self.frame,
            text="Настройки",
            font=("Segoe UI", 26, "bold"),
            bg="#F5F7FA",
            fg="#244B73"
        )
        title.pack(pady=40)

        settings = self.settings_manager.load_settings()

        tk.Label(
            self.frame,
            text="Ширина окна:",
            font=("Segoe UI", 12),
            bg="#F5F7FA"
        ).pack(pady=5)

        self.width_entry = tk.Entry(
            self.frame,
            font=("Segoe UI", 12),
            justify="center"
        )
        self.width_entry.insert(0, str(settings["window_width"]))
        self.width_entry.pack(pady=5)

        tk.Label(
            self.frame,
            text="Высота окна:",
            font=("Segoe UI", 12),
            bg="#F5F7FA"
        ).pack(pady=5)

        self.height_entry = tk.Entry(
            self.frame,
            font=("Segoe UI", 12),
            justify="center"
        )
        self.height_entry.insert(0, str(settings["window_height"]))
        self.height_entry.pack(pady=5)

        tk.Button(
            self.frame,
            text="Сохранить",
            font=("Segoe UI", 12),
            width=20,
            command=self.save_settings
        ).pack(pady=20)

        tk.Button(
            self.frame,
            text="Назад",
            font=("Segoe UI", 12),
            width=20,
            command=self.go_back
        ).pack(pady=5)

    def save_settings(self):
        try:
            width = int(self.width_entry.get())
            height = int(self.height_entry.get())

            if not 750 <= width <= 1600:
                raise ValueError("Ширина должна быть от 750 до 1600.")

            if not 550 <= height <= 1200:
                raise ValueError("Высота должна быть от 550 до 1200.")

            self.settings_manager.save_settings({
                "window_width": width,
                "window_height": height
            })

            self.root.geometry(f"{width}x{height}")
            messagebox.showinfo(
                "Настройки",
                "Настройки успешно сохранены!"
            )

        except ValueError as error:
            messagebox.showerror("Ошибка", str(error))

    def go_back(self):
        self.frame.destroy()
        self.on_back()
