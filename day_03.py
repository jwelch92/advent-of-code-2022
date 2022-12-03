import string

from lib import run

# AOC DAY 3

scores = {
    **{alpha: i for alpha, i in zip(string.ascii_lowercase, range(1, 27))},
    **{alpha: i for alpha, i in zip(string.ascii_uppercase, range(27, 53))},
}


def solve_one(data: str) -> int:
    s = 0
    print(scores)
    for line in data.splitlines():
        length = len(line)
        first, second = line[: length // 2], line[length // 2 :]
        same = list(set(first).intersection(second))[0]
        s += scores[same]
    return s


def solve_two(data: str) -> int:
    s = 0
    acc = []
    i = 0
    for line in data.splitlines():
        acc.append(line)
        if len(acc) == 3:
            same = list(set(acc[0]) & set(acc[1]) & set(acc[2]))[0]
            s += scores[same]
            acc = []
    return s


def main() -> None:
    run(3, 1, solve_one)
    run(3, 2, solve_two)


if __name__ == "__main__":
    main()
