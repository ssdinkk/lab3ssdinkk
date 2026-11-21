
from domain.board import Board
from domain.ship import Ship


board = Board()

ship = Ship(
    cells=frozenset({(0, 0), (0, 1), (0, 2)})
)

board.add_ship(ship)

print(board.shoot((0, 0)))
print(board.shoot((0, 1)))
print(board.shoot((0, 2)))
print(board.all_ships_sunk)
