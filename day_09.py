from dataclasses import dataclass
from pprint import pprint
import math
from lib import run
from typing import Any, Tuple
from operator import sub, add

# AOC DAY 9


DAY = 9

H = "H"
T = "T"

Coord = Tuple[int, int]


def dist(a: Coord, b: Coord) -> int:
    return int(math.dist(a, b))


def delta(a: Coord, b: Coord) -> Coord:
    return a[0] - b[0], a[1] - b[1]


def solve_one(data: str) -> Any:
    visited = set()
    h, t = (0, 0), (0, 0)

    for line in data.splitlines():
        direction, count = line.split(" ")
        count = int(count)
        last: Coord
        if direction == "R":
            move = (1, 0)
        elif direction == "L":
            move = (-1, 0)
        elif direction == "U":
            move = (0, 1)
        elif direction == "D":
            move = (0, -1)
        else:
            raise RuntimeError()

        for _ in range(count):
            last = tuple(h)
            h = tuple(map(add, h, move))
            d = dist(h, t)
            # print("distance", d)
            if d > 1:
                t = tuple(last)
                visited.add(t)

    # pprint(visited)
    # Too high 8915
    # 5735
    return len(visited)

def render(rope: list[tuple[int, int]]):
    # width = max(x[1] for x in rope)
    # height = max(x[0] for x in rope)
    width = 100
    height = 100
    grid = []
    for r in range(height):
        line = []
        for c in range(width):
            if (c, r) in rope:
                line.append(str(rope.index((c, r))))
            else:
                line.append(".")
            # for idx, (x, y) in enumerate(rope):
            #     if x == c and y == r:
            #         line.append(str(idx))
            #     else:
            #         line.append(".")
        grid.append(line)

    for line in reversed(grid):
        print("".join(line))



def solve_two(data: str) -> Any:
    visited = set()

    rope = [(0, 0) for _ in range(10)]
    for line in data.splitlines():
        direction, count = line.split(" ")
        count = int(count)
        for _ in range(count):
            if direction == "R":
                move = (1, 0)
            elif direction == "L":
                move = (-1, 0)
            elif direction == "U":
                move = (0, 1)
            elif direction == "D":
                move = (0, -1)
            else:
                raise RuntimeError()

            rope[0] = tuple(map(add, rope[0], move))
            for i in range(1, len(rope)):
                h = rope[i - 1]
                t = rope[i]
                d = delta(h, t)
                if abs(d[0]) > 1 or abs(d[1]) > 1:
                    dx = 0 if d[0] == 0 else 1 if d[0] > 0 else -1
                    dy = 0 if d[1] == 0 else 1 if d[1] > 0 else -1
                    rope[i] = (
                        t[0]+dx,
                        t[1]+dy
                    )
                visited.add(rope[-1])

    return len(visited)


def main(quiet: bool = False) -> None:
    # run(DAY, 1, solve_one, quiet=quiet)
    run(DAY, 2, solve_two, quiet=quiet)


if __name__ == "__main__":
    main()
