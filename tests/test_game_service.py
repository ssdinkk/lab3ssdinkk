
from application.game_service import GameService


service = GameService()

service.start_new_game()

print("Игра создана:", service.game is not None)

print(
    "Кораблей игрока:",
    len(service.game.player.board.ships)
)

print(
    "Кораблей компьютера:",
    len(service.game.computer.board.ships)
)

result = service.player_shoot((0, 0))
print("Результат выстрела:", result)

computer_result = service.computer_shoot()
print("Ход компьютера:", computer_result)
