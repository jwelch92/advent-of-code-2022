import string
from collections import defaultdict
from pprint import pprint
from typing import Any

from lib import run

# AOC DAY 5
DAY = 5
# [H]                 [Z]         [J]
# [L]     [W] [B]     [G]         [R]
# [R]     [G] [S]     [J] [H]     [Q]
# [F]     [N] [T] [J] [P] [R]     [F]
# [B]     [C] [M] [R] [Q] [F] [G] [P]
# [C] [D] [F] [D] [D] [D] [T] [M] [G]
# [J] [C] [J] [J] [C] [L] [Z] [V] [B]
# [M] [Z] [H] [P] [N] [W] [P] [L] [C]
#  1   2   3   4   5   6   7   8   9


def solve_one(data: str) -> Any:
    # -1 is the top of the stack
    m = {i: list() for i in range(1, 10)}
    raw_crates, moves = data.split("\n\n")
    # start at the first real column position 1, step by 4 to skip between possible value positions
    # Enumerate starting at 1 to match our crates 1 based index
    for line in raw_crates.splitlines()[:8]:
        for (
            count,
            idx,
        ) in enumerate(range(1, len(line), 4), start=1):
            c = line[idx]
            if c != " ":
                # Prepend to form a stack where the last element is the top
                m[count] = [c] + m[count]
    for line in moves.splitlines():
        count, src, dest = [int(i) for i in line.split(" ") if i.isdigit()]
        # Extend dest with the top `count` items in reverse order to mimic moving them one by one
        m[dest].extend(reversed(m[src][-count:]))
        # trim src by `count` items
        m[src] = m[src][:-count]
    # TQRFCBSJJ
    return "".join([m[i][-1] for i in range(1, 10)])


def solve_two(data: str) -> Any:
    # -1 is the top of the stack
    # Build the crate
    m = {i: list() for i in range(1, 10)}
    raw_crates, moves = data.split("\n\n")
    # Parse starting state
    for line in raw_crates.splitlines()[
        :8
    ]:  # 8 might be a magic number. My input only had stacks up to 8 high
        for (
            count,
            idx,
        ) in enumerate(range(1, len(line), 4), start=1):
            c = line[idx]
            if c != " ":
                m[count] = [c] + m[count]
    # process moves
    for line in moves.splitlines():
        # Get the number of crates to move, starting stack, and ending stack
        # move lines look like this
        # move 1 from 2 to 1
        count, src, dest = [int(i) for i in line.split(" ") if i.isdigit()]
        # Extend dest with the top `count` items
        m[dest].extend(m[src][-count:])
        # Trim the top `count` items from src
        m[src] = m[src][:-count:]

    # RMHFJNVFP
    return "".join([m[i][-1] for i in range(1, 10)])


def main() -> None:
    run(DAY, 1, solve_one)
    run(DAY, 2, solve_two)


if __name__ == "__main__":
    main()
