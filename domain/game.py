
from domain.player import Player


class Game:
    """Управляет ходом игры Морской бой."""

    def __init__(self, player: Player, computer: Player):
        self.player = player
        self.computer = computer
        self.current_player = player
        self.is_finished = False
        self.winner = None

    def switch_turn(self) -> None:
        """Переключает текущего игрока."""

        if self.is_finished:
            return

        if self.current_player == self.player:
            self.current_player = self.computer
        else:
            self.current_player = self.player

    def check_game_over(self) -> bool:
        """Проверяет, завершилась ли игра."""

        if self.player.has_lost():
            self.is_finished = True
            self.winner = self.computer

        elif self.computer.has_lost():
            self.is_finished = True
            self.winner = self.player

        return self.is_finished
