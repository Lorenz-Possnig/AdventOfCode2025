from typing import TypeVar, Callable, Iterable

def range_inclusive(start: int, stop: int, step: int = 1) -> range:
    return range(start, stop + 1, step)


def is_blank_or_empty(s: str) -> bool:
    return len(s) == 0 or s.isspace()


def is_not_blank_or_empty(s: str) -> bool:
    return not len(s) == 0 and not s.isspace()

T = TypeVar('T')
def count(predicate: Callable[[T], bool], iterable: Iterable[T]) -> int:
    counter = 0
    for i in iterable:
        if predicate(i):
            counter += 1
    return counter


R = TypeVar('R')
def map_indexed(operation: Callable[[int, T], R], iterable: Iterable[T]) -> map:
    return map(lambda t: operation(t[0], t[1]), enumerate(iterable))


def split_on(predicate: Callable[[T], bool], iterable: Iterable[T]) -> list[list[T]]:
    result = []
    current = list()
    for i in iterable:
        if predicate(i):
            result.append(current)
            current = list()
        else:
            current.append(i)
    if len(current) > 0:
        result.append(current)
    return result