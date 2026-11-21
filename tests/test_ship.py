
import unittest

from domain.ship import Ship


class TestShip(unittest.TestCase):

    def test_create_ship(self):
        ship = Ship(frozenset({
            (0, 0),
            (0, 1),
            (0, 2)
        }))

        self.assertFalse(ship.is_sunk)

    def test_ship_receives_hit(self):
        ship = Ship(frozenset({
            (0, 0),
            (0, 1)
        }))

        self.assertTrue(ship.receive_shot((0, 0)))
        self.assertFalse(ship.is_sunk)

    def test_ship_is_sunk(self):
        ship = Ship(frozenset({
            (0, 0),
            (0, 1)
        }))

        ship.receive_shot((0, 0))
        ship.receive_shot((0, 1))

        self.assertTrue(ship.is_sunk)

    def test_repeated_hit(self):
        ship = Ship(frozenset({
            (0, 0)
        }))

        self.assertTrue(ship.receive_shot((0, 0)))
        self.assertFalse(ship.receive_shot((0, 0)))

    def test_invalid_ship(self):
        with self.assertRaises(ValueError):
            Ship(frozenset({
                (0, 0),
                (1, 1)
            }))


if __name__ == "__main__":
    unittest.main()
