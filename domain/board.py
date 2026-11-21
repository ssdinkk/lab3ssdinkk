
from domain.ship import Ship


class Board:
    """Игровое поле размером 10 на 10."""

    SIZE = 10

    def __init__(self):
        self.ships: list[Ship] = []
        self.shots: set[tuple[int, int]] = set()

    def is_valid_coordinate(self, coordinate: tuple[int, int]) -> bool:
        """Проверяет, находится ли координата внутри поля."""

        row, col = coordinate
        return 0 <= row < self.SIZE and 0 <= col < self.SIZE

    def add_ship(self, ship: Ship) -> None:
        """Добавляет корабль на поле."""

        for cell in ship.cells:
            if not self.is_valid_coordinate(cell):
                raise ValueError("Корабль находится за пределами поля.")

        for existing_ship in self.ships:
            if ship.cells & existing_ship.cells:
                raise ValueError("Корабли не могут пересекаться.")

        self.ships.append(ship)

    def shoot(self, coordinate: tuple[int, int]) -> str:
        """Выполняет выстрел по указанной клетке."""

        if not self.is_valid_coordinate(coordinate):
            raise ValueError("Координата находится за пределами поля.")

        if coordinate in self.shots:
            return "Повторный выстрел"

        self.shots.add(coordinate)

        for ship in self.ships:
            if ship.receive_shot(coordinate):
                return "Попадание" if not ship.is_sunk else "Корабль потоплен"

        return "Мимо"

    @property
    def all_ships_sunk(self) -> bool:
        """Проверяет, уничтожены ли все корабли."""

        return bool(self.ships) and all(ship.is_sunk for ship in self.ships)
