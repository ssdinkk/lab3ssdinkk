
import unittest

from domain.game import Game
from domain.player import Player
from domain.board import Board
from domain.ship import Ship


class TestGame(unittest.TestCase):

    def setUp(self):
        self.player_board = Board()
        self.computer_board = Board()

        self.player_board.add_ship(
            Ship(frozenset({(0, 0)}))
        )

        self.computer_board.add_ship(
            Ship(frozenset({(1, 1)}))
        )

        self.player = Player("Игрок", self.player_board)
        self.computer = Player("Компьютер", self.computer_board)

        self.game = Game(self.player, self.computer)

    def test_initial_state(self):
        self.assertEqual(
            self.game.current_player,
            self.player
        )
        self.assertFalse(self.game.is_finished)
        self.assertIsNone(self.game.winner)

    def test_switch_turn(self):
        self.game.switch_turn()

        self.assertEqual(
            self.game.current_player,
            self.computer
        )

    def test_switch_turn_back(self):
        self.game.switch_turn()
        self.game.switch_turn()

        self.assertEqual(
            self.game.current_player,
            self.player
        )

    def test_player_wins(self):
        self.computer_board.shoot((1, 1))

        self.assertTrue(self.game.check_game_over())
        self.assertEqual(self.game.winner, self.player)

    def test_computer_wins(self):
        self.player_board.shoot((0, 0))

        self.assertTrue(self.game.check_game_over())
        self.assertEqual(self.game.winner, self.computer)

    def test_finished_game_does_not_switch_turn(self):
        self.computer_board.shoot((1, 1))
        self.game.check_game_over()

        self.game.switch_turn()

        self.assertEqual(
            self.game.current_player,
            self.player
        )


if __name__ == "__main__":
    unittest.main()
