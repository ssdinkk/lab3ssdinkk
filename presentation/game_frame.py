
import tkinter as tk


class GameFrame:
    """Игровой экран Морского боя."""

    def __init__(self, root, game_service, on_back):
        self.root = root
        self.game_service = game_service
        self.on_back = on_back

        self.frame = tk.Frame(root, bg="#F5F7FA")
        self.frame.pack(fill="both", expand=True)

        self.player_buttons = []
        self.computer_buttons = []

        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(
            self.frame,
            text="Морской бой",
            font=("Segoe UI", 24, "bold"),
            bg="#F5F7FA",
            fg="#244B73"
        )
        title.pack(pady=10)

        self.status_label = tk.Label(
            self.frame,
            text="Ваш ход! Выберите клетку на поле компьютера.",
            font=("Segoe UI", 11),
            bg="#F5F7FA",
            fg="#193653"
        )
        self.status_label.pack(pady=5)

        boards_frame = tk.Frame(self.frame, bg="#F5F7FA")
        boards_frame.pack(pady=10)

        self.create_board(
            boards_frame,
            "Ваше поле",
            self.player_buttons,
            0
        )

        self.create_board(
            boards_frame,
            "Поле компьютера",
            self.computer_buttons,
            1
        )

        back_button = tk.Button(
            self.frame,
            text="В меню",
            font=("Segoe UI", 11),
            command=self.go_back
        )
        back_button.pack(pady=10)

    def create_board(self, parent, title, buttons_list, column):
        board_frame = tk.Frame(parent, bg="#F5F7FA")
        board_frame.grid(row=0, column=column, padx=15)

        tk.Label(
            board_frame,
            text=title,
            font=("Segoe UI", 13, "bold"),
            bg="#F5F7FA",
            fg="#244B73"
        ).grid(row=0, column=0, columnspan=10, pady=8)

        for row in range(10):
            button_row = []

            for col in range(10):
                button = tk.Button(
                    board_frame,
                    text="",
                    width=2,
                    height=1,
                    bg="white",
                    relief="solid",
                    command=lambda r=row, c=col:
                    self.player_turn(r, c)
                    if column == 1 else None
                )

                button.grid(row=row + 1, column=col, padx=1, pady=1)
                button_row.append(button)

            buttons_list.append(button_row)

    def player_turn(self, row, col):
        self.status_label.config(
            text=f"Выстрел по клетке ({row + 1}, {col + 1})"
        )

    def go_back(self):
        self.frame.destroy()
        self.on_back()
