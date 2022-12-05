from collections import defaultdict
from pprint import pprint
from typing import Any

from lib import run

# AOC DAY 5
DAY = 5
col = 3
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
    # sub 1 when index
    m = {i: list() for i in range(1, 10)}
    # -1 is the top of the stack
    raw_crates, moves = data.split("\n\n")
    for line in raw_crates.splitlines()[:8]:
        for count, idx, in enumerate(range(1, len(line), 4), start=1):
            c = line[idx]
            if c and c != " ":
                m[count] = [c] + m[count]
    for line in moves.splitlines():
        match line.split(" "):
            case [_, count, _, start, _, end]:

                for i in range(0, int(count)):
                    m[int(end)].append(m[int(start)].pop())

    tops = []
    for i in range(1, 10):
        tops.append(m[i][-1])
    print("".join(tops))
    return "".join(tops)



def solve_two(data: str) -> Any:
    m = {i: list() for i in range(1, 10)}
    # -1 is the top of the stack
    raw_crates, moves = data.split("\n\n")
    for line in raw_crates.splitlines()[:8]:
        for count, idx, in enumerate(range(1, len(line), 4), start=1):
            c = line[idx]
            if c and c != " ":
                m[count] = [c] + m[count]
    for line in moves.splitlines():
        match line.split(" "):
            case [_, count, _, start, _, end]:
                count, start, end = int(count), int(start), int(end)
                print(count, start, end)
                print("before")
                print(m[int(start)])
                print(m[int(end)])
                print("to move")
                print(m[int(start)][-1*int(count):])

                m[int(end)].extend(m[int(start)][-1*int(count):])
                m[start] = m[start][:-1*count:]
                print("after")
                print(m[int(start)])
                print(m[int(end)])
                # input("halt")






    tops = []
    for i in range(1, 10):
        tops.append(m[i][-1])
    print("".join(tops))
    return "".join(tops)


def main() -> None:
    run(DAY, 1, solve_one)
    run(DAY, 2, solve_two)


if __name__ == "__main__":
    main()
