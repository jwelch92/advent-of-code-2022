from typing import Tuple

from lib import run

# AOC DAY 2


def parse(line: str) -> Tuple[int, int]:
    """
    Convert from chars to scores
    A X -> 0
    B Y -> 1
    C Z -> 2

    :param line:
    :return:
    """
    a, b = line.split(" ")
    return ord(a) - ord("A"), ord(b) - ord("X")


def score(you: int, me: int) -> int:
    """
    Calculate score including 3 for draw and 6 for win. Adds me + 1 to account for the 0 indexed score from parse
    :param you:
    :param me:
    :return:
    """
    return ((me - you + 1) % 3) * 3 + me + 1


def solve_one(data: str) -> int:
    acc = 0
    for l in data.splitlines():
        you, me = parse(l)
        acc += score(you, me)
    return acc


def solve_two(data: str) -> int:
    acc = 0
    for l in data.splitlines():
        you, me = parse(l)
        acc += score(you, (you + me - 1) % 3)
    return acc


def main() -> None:
    run(2, 1, solve_one)
    run(2, 2, solve_two)


if __name__ == "__main__":
    main()
