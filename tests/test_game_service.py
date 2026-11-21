
import unittest

from application.game_service import GameService


class TestGameService(unittest.TestCase):

    def setUp(self):
        self.service = GameService()
        self.service.start_new_game()

    def test_start_new_game(self):
        self.assertIsNotNone(self.service.game)
        self.assertEqual(
            len(self.service.game.player.board.ships),
            0
        )
        self.assertEqual(
            len(self.service.game.computer.board.ships),
            10
        )

    def test_player_shoot(self):
        result = self.service.player_shoot((0, 0))

        self.assertIn(
            result,
            ["Попадание", "Корабль потоплен", "Мимо"]
        )

    def test_computer_shoot(self):
        # Размещаем корабли игрока для проверки выстрела компьютера.
        self.service._place_ships(
            self.service.game.player.board
        )

        self.service.game.switch_turn()

        result = self.service.computer_shoot()

        self.assertIn(
            result,
            ["Попадание", "Корабль потоплен", "Мимо"]
        )

    def test_player_cannot_shoot_twice(self):
        self.service.player_shoot((0, 0))

        result = self.service.player_shoot((0, 1))

        self.assertEqual(
            result,
            "Сейчас ход компьютера"
        )

    def test_game_not_started(self):
        service = GameService()

        result = service.player_shoot((0, 0))

        self.assertEqual(result, "Игра не активна")


if __name__ == "__main__":
    unittest.main()
