import itertools
import sys
import timeit

from utils.utils import range_inclusive


def is_accessible(lines: list[list[str]], markers: str, i: int, j: int) -> bool:
    occupied = 0
    for k in range_inclusive(max(i - 1, 0), min(i + 1, len(lines) - 1)):
        for l in range_inclusive(max(j - 1, 0), min(j + 1, len(lines[i]) - 1)):
            if occupied == 4:
                return False
            elif k == i and l == j:
                continue
            elif lines[k][l] in markers:
                occupied += 1
    return occupied < 4


def mark_accessible(lines: list[list[str]], markers: str) -> bool:
    changed = False
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == '@' and is_accessible(lines, markers, i, j):
                lines[i][j] = 'X'
                changed = True
    return changed


def count_accessible(matrix: list[list[str]]) -> int:
    return len([matrix[i][j] for (i, j) in itertools.product(range(len(matrix)), range(len(matrix[0]))) \
         if matrix[i][j] == 'X'])


def part1(matrix: list[list[str]]) -> bool:
    return mark_accessible(matrix, "@X")


def part2(matrix: list[list[str]]) -> bool:
    return mark_accessible(matrix, "@")


def main() -> None:
    with open(f'../../resources/day4/{sys.argv[1]}', 'r') as h:
        matrix: list[list[str]] = list(map(lambda s: list(s), h.read().split('\n')))
        changed = part1(matrix)
        print(f'Part 1: {count_accessible(matrix)}')
        while changed:
            changed = part2(matrix)
        print(f'Part 2: {count_accessible(matrix)}')


if __name__ == '__main__':
    execution_time = timeit.timeit(main, number=1)
    print(f'Took {round(execution_time, 4)} Seconds to solve')