
from domain.ship import Ship


ship = Ship(cells=frozenset({(0, 0), (0, 1), (0, 2)}))

print(ship.receive_shot((0, 0)))
print(ship.receive_shot((0, 1)))
print(ship.receive_shot((0, 2)))
print(ship.is_sunk)
