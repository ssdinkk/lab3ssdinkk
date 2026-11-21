
import tkinter as tk


class RulesFrame:
    """Экран с правилами игры."""

    def __init__(self, root, on_back):
        self.root = root
        self.on_back = on_back

        self.frame = tk.Frame(root, bg="#F5F7FA")
        self.frame.pack(fill="both", expand=True)

        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(
            self.frame,
            text="Правила игры",
            font=("Segoe UI", 26, "bold"),
            bg="#F5F7FA",
            fg="#244B73"
        )
        title.pack(pady=35)

        rules = (
            "1. В игре участвуют два игрока: вы и компьютер.\n\n"
            "2. У каждого игрока есть поле размером 10 на 10 клеток.\n\n"
            "3. На поле размещается флот из 10 кораблей:\n"
            "   один четырёхпалубный, два трёхпалубных,\n"
            "   три двухпалубных и четыре однопалубных.\n\n"
            "4. Игроки стреляют по очереди.\n\n"
            "5. Попадание означает, что в клетке находится корабль.\n\n"
            "6. Побеждает тот, кто первым потопит весь флот противника."
        )

        rules_label = tk.Label(
            self.frame,
            text=rules,
            font=("Segoe UI", 12),
            bg="#F5F7FA",
            fg="#193653",
            justify="left",
            wraplength=650
        )
        rules_label.pack(padx=40, pady=15)

        back_button = tk.Button(
            self.frame,
            text="Назад",
            font=("Segoe UI", 12),
            width=20,
            command=self.go_back
        )
        back_button.pack(pady=25)

    def go_back(self):
        self.frame.destroy()
        self.on_back()
