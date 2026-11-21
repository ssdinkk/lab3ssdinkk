
import unittest

from domain.player import Player
from domain.board import Board
from domain.ship import Ship


class TestPlayer(unittest.TestCase):

    def test_create_player(self):
        player = Player("Игрок", Board())

        self.assertEqual(player.name, "Игрок")
        self.assertIsInstance(player.board, Board)

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            Player("   ", Board())

    def test_player_has_not_lost(self):
        board = Board()
        board.add_ship(
            Ship(frozenset({(0, 0)}))
        )

        player = Player("Игрок", board)

        self.assertFalse(player.has_lost())

    def test_player_has_lost(self):
        board = Board()
        ship = Ship(frozenset({(0, 0)}))
        board.add_ship(ship)
        board.shoot((0, 0))

        player = Player("Игрок", board)

        self.assertTrue(player.has_lost())


if __name__ == "__main__":
    unittest.main()
