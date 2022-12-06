from collections import deque

from lib import run
from typing import Any
# AOC DAY 6


DAY = 6


def solve_one(data: str) -> Any:
    b = deque()
    for i, c in enumerate(data):
        if len(b) == 4:
            if len(set(b)) == 4 and i > 4:
                return i
            b.popleft()
        b.append(c)


def solve_two(data: str) -> Any:
    b = deque()
    for i, c in enumerate(data):
        if len(b) == 14:
            if len(set(b)) == 14 and i > 4:
                return i
            b.popleft()
        b.append(c)


def main() -> None:
    run(DAY, 1, solve_one)
    run(DAY, 2, solve_two)


if __name__ == "__main__":
    main()
