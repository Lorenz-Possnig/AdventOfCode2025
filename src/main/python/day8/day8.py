import math
import operator
import sys
import timeit
from functools import reduce
from typing import Optional


class Point:
    x: int
    y: int
    z: int
    head: 'Point' = None

    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z

    def find_head(self) -> 'Point':
        candidate = self
        while candidate.head is not None:
            candidate = candidate.head
        return candidate

    def __eq__(self, other) -> bool:
        if self is other: return True
        if type(other) is not Point: return False
        return self.x == other.x \
            and self.y == other.y \
            and self.z == other.z

    def __hash__(self):
        result = self.x
        result = 31 * result + self.y
        result = 31 * result + self.z
        return result

    @staticmethod
    def from_string(s: str) -> 'Point':
        ls = list(map(int, s.split(',')))
        return Point(ls[0], ls[1], ls[2])


class PointPair:
    p: Point
    q: Point
    euclid: Optional[float] = None

    def __init__(self, p: Point, q: Point) -> None:
        self.p = p
        self.q = q

    def distance(self):
        if self.euclid is None:
            self.euclid = math.sqrt(
                sum([
                    (self.p.x - self.q.x) ** 2,
                    (self.p.y - self.q.y) ** 2,
                    (self.p.z - self.q.z) ** 2
                ]))
        return self.euclid

    def __contains__(self, item: Point):
        return self.p == item or self.q == item

    def __lt__(self, other):
        return self.distance() < other.distance()


def main() -> None:
    input_file = f'../../resources/day8/{sys.argv[1]}'
    num_connections = 10 if input_file.endswith('demo') else 1000
    with open(input_file, 'r') as h:
        points: list[Point] = list(map(Point.from_string, h.read().split('\n')))
        distances: list[PointPair] = reduce(lambda a, b: a + b, list(map(lambda i: \
                                                                             list(map(lambda j: \
                                                                                          PointPair(points[i],
                                                                                                    points[j]),
                                                                                      range(i + 1, len(points)))),
                                                                         range(len(points)))), [])
        distances.sort()
        circuits: dict[Point, int] = dict()
        connections = 0
        for distance in distances:
            head1 = distance.p.find_head()
            size1 = circuits.get(head1)
            head2 = distance.q.find_head()
            size2 = circuits.get(head2)
            if size1 is None and size2 is None:
                distance.q.head = distance.p
                circuits[distance.p] = 2
            elif size1 is not None and size2 is None:
                distance.q.head = head1
                circuits[head1] = size1 + 1
            elif size1 is None and size2 is not None:
                distance.p.head = head2
                circuits[head2] = size2 + 1
            elif head1 != head2:
                head2.head = head1
                del circuits[head2]
                circuits[head1] = size1 + size2
            else:
                # last case is head1 == head2 -> nothing to do
                pass
            connections += 1
            if connections == num_connections:
                values = list(circuits.values())
                values.sort(reverse=True)
                result = reduce(operator.mul, values[:3])
                print(f'Part 1: {result}')
            if len(circuits) == 1 and len(points) in circuits.values():
                result = distance.p.x * distance.q.x
                print(f'Part 2: {result}')
                break


if __name__ == '__main__':
    execution_time = timeit.timeit(main, number=1)
    print(f'Took {round(execution_time, 4)} Seconds to solve')
