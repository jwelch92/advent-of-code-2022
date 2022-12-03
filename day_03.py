import string
from lib import run
from more_itertools import grouper

# AOC DAY 3

scores = {
    **{alpha: i for alpha, i in zip(string.ascii_lowercase, range(1, 27))},
    **{alpha: i for alpha, i in zip(string.ascii_uppercase, range(27, 53))},
}


def solve_one(data: str) -> int:
    s = 0
    for line in data.splitlines():
        length = len(line)
        first, second = line[: length // 2], line[length // 2 :]
        same = list(set(first).intersection(second))[0]
        s += scores[same]
    return s


def solve_two(data: str) -> int:
    s = 0
    for a, b, c in grouper(data.splitlines(), 3, incomplete="ignore"):
        same = list(set(a) & set(b) & set(c))[0]
        s += scores[same]
    return s


def main() -> None:
    run(3, 1, solve_one)
    run(3, 2, solve_two)


if __name__ == "__main__":
    main()
