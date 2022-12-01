from typing import Any

from lib import run


def solve_one(data: str) -> int:
    return max(
        [sum([int(i) for i in chunk.splitlines()]) for chunk in data.split("\n\n")]
    )


def solve_two(data: str) -> int:
    return sum(
        sorted(
            sum([int(i) for i in chunk.splitlines()]) for chunk in data.split("\n\n")
        )[-3:]
    )


# TODO templatize this
def main() -> None:
    run(1, 1, solve_one)
    run(1, 2, solve_two)


if __name__ == "__main__":
    main()
