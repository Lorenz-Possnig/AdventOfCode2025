import itertools
import sys
import timeit

from utils.utils import is_not_blank_or_empty, count


class IdRange:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end

    def __contains__(self, item) -> bool:
        return self.start <= item <= self.end

    def __len__(self) -> int:
        return self.end - self.start + 1

    @staticmethod
    def merge_ranges(ranges: list) -> list:
        result = []
        ranges.sort(key=lambda r: r.start)
        for i in range(len(ranges)):
            start = ranges[i].start
            end = ranges[i].end
            if len(result) > 0 and result[-1].end >= end:
                continue
            for j in range(i + 1, len(ranges)):
                if ranges[j].start <= end:
                    end = max(end, ranges[j].end)
            result.append(IdRange(start, end))
        return result


def main() -> None:
    with open(f'../../resources/day5/{sys.argv[1]}', 'r') as h:
        lines = h.read().split('\n')
        id_ranges = list(map(lambda x: (lambda r: IdRange(int(r[0]), int(r[1])))(x.split('-')),
                        itertools.takewhile(is_not_blank_or_empty, lines)))
        ingredient_ids = list(map(int, list(itertools.dropwhile(is_not_blank_or_empty, lines))[1:]))
        part1 = count(lambda ingredient_id: any(map(lambda id_range: ingredient_id in id_range, id_ranges)), ingredient_ids)
        print(f'Part 1: {part1}')
        merged_ranges = IdRange.merge_ranges(id_ranges)
        part2 = sum(map(lambda x: len(x), merged_ranges))
        print(f'Part 2: {part2}')


if __name__ == '__main__':
    execution_time = timeit.timeit(main, number=1)
    print(f'Took {round(execution_time, 4)} Seconds to solve')