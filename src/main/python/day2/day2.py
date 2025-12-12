import sys
import timeit


# part 1
def is_silly(i: int) -> bool:
    st = str(i)
    l = len(st)
    mid = l // 2
    return l % 2 == 0 and st[0: mid] == st[mid:]


# part 2
def is_very_silly(i: int) -> bool:
    st = str(i)
    length = len(st)
    for j in range(1, (length // 2) + 1):
        pattern = st[:j] * (length // j)
        if pattern == st:
            return True
    return False


def main() -> None:
    with open(f'../../resources/day2/{sys.argv[1]}', 'r') as h:
        contents = h.read()
        ranges = [range(int(r[0]), int(r[1]) + 1) for r in map(lambda s: s.split('-'), contents.split(','))]
        silly_ids = [i for r in ranges for i in r if is_silly(i)]
        print(f'Part 1: {sum(silly_ids)}')
        very_silly_ids = [i for r in ranges for i in r if is_very_silly(i)]
        print(f'Part 2: {sum(very_silly_ids)}')

if __name__ == '__main__':
    a = timeit.timeit(main, number=1)
    print(f'Took {round(a,4)} Seconds to solve')
