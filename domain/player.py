
from dataclasses import dataclass

from domain.board import Board


@dataclass
class Player:
    """Класс участника игры."""

    name: str
    board: Board

    def __post_init__(self):
        if not self.name.strip():
            raise ValueError("Имя игрока не может быть пустым.")

    def has_lost(self) -> bool:
        """Проверяет, проиграл ли игрок."""

        return self.board.all_ships_sunk
