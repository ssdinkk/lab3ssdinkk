
import random

from domain.board import Board
from domain.game import Game
from domain.player import Player
from domain.ship import Ship


class GameService:
    """Сервис управления игровой партией."""

    def __init__(self):
        self.game = None


    def start_new_game(self):
        """Создаёт новую игру с пустым полем игрока."""

        player = Player("Игрок", Board())
        computer = Player("Компьютер", Board())

        # Компьютер получает случайно расставленные корабли.
        self._place_ships(computer.board)

        # Поле игрока остаётся пустым для ручной расстановки.
        self.game = Game(player, computer)


    def _place_ships(self, board: Board):
        """Автоматически размещает флот на поле."""

        ship_sizes = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

        for size in ship_sizes:
            placed = False

            while not placed:
                horizontal = random.choice([True, False])
                row = random.randint(0, 9)
                col = random.randint(0, 9)

                if horizontal:
                    cells = {
                        (row, col + i) for i in range(size)
                    }
                else:
                    cells = {
                        (row + i, col) for i in range(size)
                    }

                if any(
                    not board.is_valid_coordinate(cell)
                    for cell in cells
                ):
                    continue

                if any(
                    abs(row1 - row2) <= 1
                    and abs(col1 - col2) <= 1
                    for ship in board.ships
                    for row1, col1 in ship.cells
                    for row2, col2 in cells
                ):
                    continue

                board.add_ship(Ship(frozenset(cells)))
                placed = True


    def player_shoot(self, coordinate):
        """Обрабатывает выстрел игрока."""

        if self.game is None or self.game.is_finished:
            return "Игра не активна"

        if self.game.current_player != self.game.player:
            return "Сейчас ход компьютера"

        result = self.game.computer.board.shoot(coordinate)
        self.game.check_game_over()

        if not self.game.is_finished:
            self.game.switch_turn()

        return result



    def computer_shoot(self):
        """Выполняет случайный выстрел компьютера."""

        if self.game is None or self.game.is_finished:
            return "Игра не активна"

        if self.game.current_player != self.game.computer:
            return "Сейчас ход игрока"

        board = self.game.player.board

        available_cells = [
            (row, col)
            for row in range(10)
            for col in range(10)
            if (row, col) not in board.shots
        ]

        if not available_cells:
            return "Нет доступных клеток"

        coordinate = random.choice(available_cells)
        result = board.shoot(coordinate)

        self.game.check_game_over()

        if not self.game.is_finished:
            self.game.switch_turn()

        return result

