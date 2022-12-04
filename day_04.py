from more_itertools import pairwise, flatten

from lib import run, wait_for_it

# AOC DAY 4
DAY = 4


def solve_one(data: str) -> int:
    return sum(
        flatten(
            [
                [
                    int(a.issubset(b) or b.issubset(a))
                    for a, b in pairwise(
                        set(range(x, y + 1))
                        for x, y in (
                            (int(i) for i in a.split("-")) for a in line.split(",")
                        )
                    )
                ]
                for line in data.splitlines()
            ]
        )
    )


def solve_two(data: str) -> int:
    answer = 0
    for line in data.splitlines():
        a, b = (
            set(range(x, y + 1))
            for x, y in ((int(i) for i in a.split("-")) for a in line.split(","))
        )
        if a.intersection(b):
            answer += 1

    return answer


def main() -> None:
    run(DAY, 1, solve_one)
    run(DAY, 2, solve_two)


if __name__ == "__main__":
    main()
