
from dataclasses import dataclass, field


@dataclass
class Ship:
    """Класс, описывающий корабль в игре."""

    cells: frozenset[tuple[int, int]]
    hits: set[tuple[int, int]] = field(default_factory=set)

    def __post_init__(self):
        if not self.cells:
            raise ValueError("Корабль должен содержать хотя бы одну клетку.")

        rows = {row for row, col in self.cells}
        cols = {col for row, col in self.cells}

        if len(rows) > 1 and len(cols) > 1:
            raise ValueError("Корабль должен располагаться по прямой.")

        coordinates = sorted(self.cells)

        if len(rows) == 1:
            positions = sorted(col for row, col in self.cells)
        else:
            positions = sorted(row for row, col in self.cells)

        if positions != list(range(positions[0], positions[-1] + 1)):
            raise ValueError("Клетки корабля должны располагаться рядом.")

        if not self.hits.issubset(self.cells):
            raise ValueError("Попадания должны находиться внутри корабля.")

    def receive_shot(self, coordinate: tuple[int, int]) -> bool:
        """Обрабатывает выстрел по кораблю."""

        if coordinate not in self.cells or coordinate in self.hits:
            return False

        self.hits.add(coordinate)
        return True

    @property
    def is_sunk(self) -> bool:
        """Проверяет, потоплен ли корабль."""

        return self.hits == self.cells
