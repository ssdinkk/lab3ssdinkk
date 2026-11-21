
from domain.board import Board
from domain.player import Player


player = Player(
    name="Игрок",
    board=Board()
)

print(player.name)
print(player.has_lost())
