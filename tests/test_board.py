
import unittest

from domain.board import Board
from domain.ship import Ship


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_create_board(self):
        self.assertEqual(len(self.board.ships), 0)
        self.assertEqual(len(self.board.shots), 0)

    def test_add_ship(self):
        ship = Ship(frozenset({
            (0, 0),
            (0, 1)
        }))

        self.board.add_ship(ship)

        self.assertEqual(len(self.board.ships), 1)

    def test_ship_out_of_bounds(self):
        ship = Ship(frozenset({
            (0, 9),
            (0, 10)
        }))

        with self.assertRaises(ValueError):
            self.board.add_ship(ship)

    def test_ships_cannot_overlap(self):
        first_ship = Ship(frozenset({
            (0, 0),
            (0, 1)
        }))

        second_ship = Ship(frozenset({
            (0, 1),
            (0, 2)
        }))

        self.board.add_ship(first_ship)

        with self.assertRaises(ValueError):
            self.board.add_ship(second_ship)

    def test_missed_shot(self):
        self.assertEqual(
            self.board.shoot((5, 5)),
            "Мимо"
        )

    def test_successful_hit(self):
        ship = Ship(frozenset({
            (0, 0)
        }))

        self.board.add_ship(ship)

        self.assertEqual(
            self.board.shoot((0, 0)),
            "Корабль потоплен"
        )

    def test_repeated_shot(self):
        self.board.shoot((5, 5))

        self.assertEqual(
            self.board.shoot((5, 5)),
            "Повторный выстрел"
        )

    def test_invalid_coordinate(self):
        with self.assertRaises(ValueError):
            self.board.shoot((10, 10))


if __name__ == "__main__":
    unittest.main()
