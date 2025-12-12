import copy
import functools
import sys
import timeit


def part1(matrix: list[list[str]], i: int, j: int) -> int:
    if len(matrix) == i \
        or j < 0 \
        or j > len(matrix[0]) \
        or matrix[i][j] == '|': return 0
    elif matrix[i][j] == '^':
        return 1 + part1(matrix, i, j - 1) + part1(matrix, i, j + 1)
    else:
        matrix[i][j] = '|'
        return part1(matrix, i + 1, j)


@functools.cache
def _part2(matrix: tuple[tuple[str]], i: int, j: int) -> int:
    if i == len(matrix) \
        or j < 0 \
        or j > len(matrix[0]):
            return 0
    elif matrix[i][j] == '^':
        return 1 + _part2(matrix, i, j - 1) + _part2(matrix, i, j + 1)
    else:
        return _part2(matrix, i + 1, j)


def part2(matrix: tuple[tuple[str]], i: int, j: int) -> int:
    return 1 + _part2(matrix, i, j)


def main() -> None:
    with open(f'../../resources/day7/{sys.argv[1]}', 'r') as h:
        matrix = list(map(list, h.read().split('\n')))
        entry_point = matrix[0].index('S')
        result1 = part1(copy.deepcopy(matrix), 1, entry_point)
        print(f'Part 1: {result1}')
        frozen_matrix = tuple(map(tuple, matrix))
        result2 = part2(frozen_matrix, 1, entry_point)
        print(f'Part 2: {result2}')


if __name__ == '__main__':
    execution_time = timeit.timeit(main, number=1)
    print(f'Took {round(execution_time, 4)} Seconds to solve')