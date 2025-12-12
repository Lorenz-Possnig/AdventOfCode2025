import re
import sys
import timeit
from functools import partial, reduce
from typing import TypeVar, Callable

from utils.utils import map_indexed, split_on, is_blank_or_empty

T = TypeVar("T")
def transpose(matrix: list[list[T]]) -> list[list[T]]:
    return list(map(lambda i:
                        list(map(lambda j:
                                     matrix[j][i],
                                 range(len(matrix)))),
                    range(len(matrix[0]))))


def add(a: int, b:int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


def get_operation(s: str) -> Callable[[int, int], int]:
    match s.strip():
        case '+':
            return add
        case '*':
            return multiply
    raise Exception('Unknown Operator')


def main() -> None:
    with open(f'../../resources/day6/{sys.argv[1]}', 'r') as h:
        lines = h.read().split("\n")
        number_lines = lines[:-1]
        numbers = transpose(list(map(lambda line:
                               list(map(lambda s:
                                       int(s.strip()),
                                   re.split(r' +', line.strip()))),
                                     number_lines)))
        operations = list(map(get_operation, re.split(r' +', lines[-1])))
        part1 = sum(map_indexed(lambda i, op: reduce(op, numbers[i]), operations))
        print(f'Part 1: {part1}')
        max_len = max(map(len, number_lines))
        ceph_math = transpose(list(map(lambda s: s + (' ' * (max_len - len(s))), number_lines)))
        ceph_math = map(lambda line: ''.join(line), ceph_math)
        ceph_math = split_on(is_blank_or_empty, ceph_math)
        ceph_math = map(lambda s: s[::-1], ceph_math)
        ceph_math = list(map(lambda ls: list(map(lambda s: int(s.strip()), ls)), ceph_math))
        part2 = sum(map_indexed(lambda i, op: reduce(op, ceph_math[i]), operations[::-1]))
        print(f'Part 2: {part2}')


if __name__ == '__main__':
    execution_time = timeit.timeit(main, number=1)
    print(f'Took {round(execution_time, 4)} Seconds to solve')