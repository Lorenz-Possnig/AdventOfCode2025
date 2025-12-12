import functools
import sys
import timeit


@functools.cache
def find_max_joltage(batteries: str, amount: int) -> int:
    if amount == 0:
        return 0
    if len(batteries) == amount:
        return int(batteries)
    s = batteries[1:]
    i = amount - 1
    a = (10 ** i) * int(batteries[0]) + find_max_joltage(s, i)
    b = find_max_joltage(s, amount)
    return a if a > b else b


def main() -> None:
    with open(f'../../resources/day3/{sys.argv[1]}', 'r') as h:
        content = h.read()
        lines = content.split('\n')
        print(f'Part 1: {sum([find_max_joltage(i, 2) for i in lines])}')
        print(f'Part 2: {sum([find_max_joltage(i, 12) for i in lines])}')
        print(f'Extra credit: {sum([find_max_joltage(i, 50) for i in lines])}')

if __name__ == '__main__':
    execution_time = timeit.timeit(main, number=1)
    print(f'Took {round(execution_time, 4)} Seconds to solve')