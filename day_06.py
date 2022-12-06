from more_itertools import sliding_window

from lib import run
from typing import Any
from typing import Any

from more_itertools import sliding_window

from lib import run

# AOC DAY 6


DAY = 6


def solve_one(data: str) -> Any:
    return (
        next(
            (
                data.index("".join(c))
                for c in sliding_window(data, 4)
                if len(set(c)) == 4
            )
        )
        + 4
    )


def solve_two(data: str) -> Any:
    return (
        next(
            (
                data.index("".join(c))
                for c in sliding_window(data, 14)
                if len(set(c)) == 14
            )
        )
        + 14
    )


def main() -> None:
    run(DAY, 1, solve_one)
    run(DAY, 2, solve_two)


if __name__ == "__main__":
    main()
