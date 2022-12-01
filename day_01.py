import bisect
from typing import Any

from lib import run

# TODO write something to group emtpy line delimited blocks

def solve_one(data: str) -> int:
    lines = data.splitlines()
    max = -1
    acc = 0
    for l in lines:
        if not l:
            if acc > max:
                max = acc
            acc = 0
            continue
        acc += int(l)
    return max


def solve_two(data: str) -> Any:
    lines = data.splitlines()
    m = []
    acc = 0
    for l in lines:
        if not l:
            bisect.insort(m, acc)
            acc = 0
            continue
        acc += int(l)
    return sum(m[-3:])


# TODO templatize this
def main() -> None:
    run(1, 1, solve_one)
    run(1, 2, solve_two)


if __name__ == "__main__":
    main()
