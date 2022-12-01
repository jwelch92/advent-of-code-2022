import bisect
from typing import Any

from lib import run


def solve_one(data: str) -> int:
    m = 0
    for chunk in data.split("\n\n"):
        a = sum([int(i) for i in chunk.splitlines()])
        if a > m:
            m = a
    return m


def solve_two(data: str) -> Any:
    m = []
    for chunk in data.split("\n\n"):
        bisect.insort(m, sum([int(i) for i in chunk.splitlines()]))
    return sum(m[-3:])


# TODO templatize this
def main() -> None:
    run(1, 1, solve_one)
    run(1, 2, solve_two)


if __name__ == "__main__":
    main()
