
import tkinter as tk
from tkinter import messagebox


class GameFrame:
    """Игровой экран Морского боя."""

    def __init__(self, root, game_service, on_back):
        self.root = root
        self.game_service = game_service
        self.on_back = on_back
        self.computer_turn_pending = False

        self.frame = tk.Frame(root, bg="#F5F7FA")
        self.frame.pack(fill="both", expand=True)

        self.player_buttons = []
        self.computer_buttons = []

        self.create_widgets()
        self.update_boards()

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
            text="Ваш ход! Выберите клетку компьютера.",
            font=("Segoe UI", 11),
            bg="#F5F7FA",
            fg="#193653"
        )
        self.status_label.pack(pady=5)

        boards_frame = tk.Frame(
            self.frame,
            bg="#F5F7FA"
        )
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
        board_frame = tk.Frame(
            parent,
            bg="#F5F7FA"
        )
        board_frame.grid(
            row=0,
            column=column,
            padx=15
        )

        tk.Label(
            board_frame,
            text=title,
            font=("Segoe UI", 13, "bold"),
            bg="#F5F7FA",
            fg="#244B73"
        ).grid(
            row=0,
            column=0,
            columnspan=10,
            pady=8
        )

        for row in range(10):
            button_row = []

            for col in range(10):
                if column == 1:
                    button = tk.Button(
                        board_frame,
                        text="",
                        width=2,
                        height=1,
                        bg="white",
                        relief="solid",
                        command=lambda r=row, c=col:
                        self.player_turn(r, c)
                    )
                else:
                    button = tk.Label(
                        board_frame,
                        text="",
                        width=2,
                        height=1,
                        bg="white",
                        relief="solid",
                        borderwidth=1
                    )

                button.grid(
                    row=row + 1,
                    column=col,
                    padx=1,
                    pady=1
                )

                button_row.append(button)

            buttons_list.append(button_row)

    def player_turn(self, row, col):
        if self.computer_turn_pending:
            return

        if self.game_service.game.is_finished:
            return

        try:
            result = self.game_service.player_shoot(
                (row, col)
            )

            if result == "Повторный выстрел":
                self.status_label.config(
                    text="Вы уже стреляли в эту клетку!"
                )
                return

            self.update_boards()

            if self.game_service.game.is_finished:
                self.show_game_result()
                return

            self.computer_turn_pending = True

            self.status_label.config(
                text=f"{result}! Ход компьютера..."
            )

            self.root.after(
                700,
                self.computer_turn
            )

        except ValueError as error:
            messagebox.showerror(
                "Ошибка",
                str(error)
            )

    def computer_turn(self):
        if self.game_service.game.is_finished:
            self.computer_turn_pending = False
            return

        try:
            result = self.game_service.computer_shoot()

            self.update_boards()

            self.computer_turn_pending = False

            if self.game_service.game.is_finished:
                self.show_game_result()
            else:
                self.status_label.config(
                    text=f"Компьютер: {result}. Ваш ход!"
                )

        except ValueError as error:
            self.computer_turn_pending = False

            messagebox.showerror(
                "Ошибка",
                str(error)
            )

    def update_boards(self):
        player_board = self.game_service.game.player.board
        computer_board = self.game_service.game.computer.board

        for row in range(10):
            for col in range(10):
                coordinate = (row, col)

                # Отображение поля игрока.
                player_button = self.player_buttons[row][col]

                is_player_ship = any(
                    coordinate in ship.cells
                    for ship in player_board.ships
                )

                if coordinate in player_board.shots:
                    if is_player_ship:
                        player_button.config(
                            text="×",
                            bg="#FCA5A5"
                        )
                    else:
                        player_button.config(
                            text="•",
                            bg="#DBEAFE"
                        )

                elif is_player_ship:
                    player_button.config(
                        text="■",
                        bg="#244B73",
                        fg="white"
                    )

                else:
                    player_button.config(
                        text="",
                        bg="white",
                        fg="black"
                    )

                # Отображение поля компьютера.
                # Корабли компьютера скрыты.

                computer_button = self.computer_buttons[row][col]

                if coordinate in computer_board.shots:
                    is_hit = any(
                        coordinate in ship.cells
                        for ship in computer_board.ships
                    )

                    if is_hit:
                        computer_button.config(
                            text="×",
                            bg="#FCA5A5",
                            state="disabled"
                        )
                    else:
                        computer_button.config(
                            text="•",
                            bg="#DBEAFE",
                            state="disabled"
                        )

                else:
                    computer_button.config(
                        text="",
                        bg="white",
                        state="normal"
                    )

    def show_game_result(self):
        winner = self.game_service.game.winner

        if winner == self.game_service.game.player:
            message = "Поздравляем! Вы победили!"
        else:
            message = "Компьютер победил!"

        self.status_label.config(
            text=message
        )

        messagebox.showinfo(
            "Игра окончена",
            message
        )

    def go_back(self):
        self.frame.destroy()
        self.on_back()

