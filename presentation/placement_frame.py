
import tkinter as tk
from tkinter import messagebox

from domain.ship import Ship


class PlacementFrame:
    """Экран ручной расстановки кораблей."""

    SHIP_SIZES = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

    def __init__(self, root, game_service, on_start, on_back):
        self.root = root
        self.game_service = game_service
        self.on_start = on_start
        self.on_back = on_back

        self.board = self.game_service.game.player.board
        self.ships_to_place = self.SHIP_SIZES.copy()
        self.orientation = "horizontal"

        self.frame = tk.Frame(root, bg="#F5F7FA")
        self.frame.pack(fill="both", expand=True)

        self.buttons = []

        self.create_widgets()
        self.update_board()

    def create_widgets(self):
        tk.Label(
            self.frame,
            text="Расстановка кораблей",
            font=("Segoe UI", 24, "bold"),
            bg="#F5F7FA",
            fg="#244B73"
        ).pack(pady=10)

        self.status_label = tk.Label(
            self.frame,
            text="Нажмите на поле, чтобы поставить корабль длиной 4 клетки.",
            font=("Segoe UI", 11),
            bg="#F5F7FA",
            fg="#193653"
        )
        self.status_label.pack(pady=5)

        self.orientation_button = tk.Button(
            self.frame,
            text="Ориентация: горизонтальная",
            font=("Segoe UI", 10),
            command=self.change_orientation
        )
        self.orientation_button.pack(pady=5)

        board_frame = tk.Frame(self.frame, bg="#F5F7FA")
        board_frame.pack(pady=10)

        for row in range(10):
            button_row = []

            for col in range(10):
                button = tk.Button(
                    board_frame,
                    text="",
                    width=3,
                    height=1,
                    bg="white",
                    relief="solid",
                    command=lambda r=row, c=col: self.place_ship(r, c)
                )

                button.grid(
                    row=row,
                    column=col,
                    padx=1,
                    pady=1
                )

                button_row.append(button)

            self.buttons.append(button_row)

        tk.Button(
            self.frame,
            text="Автоматическая расстановка",
            command=self.auto_place
        ).pack(pady=5)

        self.start_button = tk.Button(
            self.frame,
            text="Начать игру",
            state="disabled",
            command=self.start_game
        )
        self.start_button.pack(pady=5)

        tk.Button(
            self.frame,
            text="Назад",
            command=self.go_back
        ).pack(pady=5)

    def change_orientation(self):
        if self.orientation == "horizontal":
            self.orientation = "vertical"
            text = "Ориентация: вертикальная"
        else:
            self.orientation = "horizontal"
            text = "Ориентация: горизонтальная"

        self.orientation_button.config(text=text)

    def place_ship(self, row, col):
        if not self.ships_to_place:
            return

        size = self.ships_to_place[0]

        if self.orientation == "horizontal":
            cells = {
                (row, col + i) for i in range(size)
            }
        else:
            cells = {
                (row + i, col) for i in range(size)
            }

        if any(
            not self.board.is_valid_coordinate(cell)
            for cell in cells
        ):
            self.status_label.config(
                text="Не хватает места! Выберите другую клетку."
            )
            return

        for ship in self.board.ships:
            for r1, c1 in ship.cells:
                for r2, c2 in cells:
                    if abs(r1 - r2) <= 1 and abs(c1 - c2) <= 1:
                        self.status_label.config(
                            text="Корабли не должны касаться друг друга!"
                        )
                        return

        try:
            self.board.add_ship(Ship(frozenset(cells)))
        except ValueError as error:
            messagebox.showerror("Ошибка", str(error))
            return

        self.ships_to_place.pop(0)
        self.update_board()

        if self.ships_to_place:
            size = self.ships_to_place[0]
            self.status_label.config(
                text=f"Теперь разместите корабль длиной {size}."
            )
        else:
            self.status_label.config(
                text="Все корабли размещены! Можно начинать игру."
            )
            self.start_button.config(state="normal")

    def update_board(self):
        occupied = {
            cell
            for ship in self.board.ships
            for cell in ship.cells
        }

        for row in range(10):
            for col in range(10):
                if (row, col) in occupied:
                    self.buttons[row][col].config(
                        text="■",
                        bg="#244B73",
                        fg="white"
                    )
                else:
                    self.buttons[row][col].config(
                        text="",
                        bg="white",
                        fg="black"
                    )


    def auto_place(self):
        """Автоматически размещает корабли игрока."""

        self.board.ships.clear()
        self.board.shots.clear()

        self.game_service._place_ships(self.board)

        self.ships_to_place.clear()

        self.update_board()

        self.status_label.config(
            text="Корабли расставлены автоматически!"
        )

        self.start_button.config(state="normal")


    def start_game(self):
        self.frame.destroy()
        self.on_start()

    def go_back(self):
        self.frame.destroy()
        self.on_back()
