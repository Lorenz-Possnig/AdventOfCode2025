import sys
import timeit


class Point:
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self is other: return True
        if type(other) is not Point: return False
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        result = self.x
        result = 41 * result + self.y
        return result

    def __str__(self):
        return f'({self.x}, {self.y})'

    @staticmethod
    def from_str(s: str):
        split = s.split(',')
        return Point(int(split[0]), int(split[1]))


class Rectangle:
    p: Point
    q: Point
    _a = None

    def __init__(self, p: Point, q: Point) -> None:
        self.p = p
        self.q = q

    def area(self) -> int:
        if self._a is None:
            a = 1 + abs(self.q.x - self.p.x)
            b = 1 + abs(self.p.y - self.q.y)
            self._a = a * b
        return self._a

    def __eq__(self, other):
        if self is other: return True
        if type(other) is not Rectangle: return False
        return (self.p == other.p and self.q == other.q) or (self.p == other.q and self.q == other.p)

    def __hash__(self):
        result = self.p.__hash__()
        result = 31 * result + self.q.__hash__()
        return result

    def __lt__(self, other):
        return self.area() < other.area()

    def __str__(self):
        return f'[{self.p}, {self.q}]'

def main() -> None:
    with open(f'../../resources/day9/{sys.argv[1]}', 'r') as h:
        points = list(map(Point.from_str, h.read().splitlines()))
        rectangles = set()
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                rectangles.add(Rectangle(points[i], points[j]))
        part1 = max(rectangles)
        print(f'Part 1: {part1.area()}')


if __name__ == '__main__':
    execution_time = timeit.timeit(main, number=1)
    print(f'Took {round(execution_time, 4)} Seconds to solve')
