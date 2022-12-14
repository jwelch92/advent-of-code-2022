from collections import defaultdict

from more_itertools import sliding_window

from lib import run
from typing import Any


# AOC DAY 14


DAY = 14

AIR = "."
ROCK = "#"
SAND = "o"


def print_cave(cave: list[tuple[int, int], str], highlight=None):
    hs, he = min(x[1] for x in cave), max(x[1] for x in cave)
    ws, we = min(x[0] for x in cave), max(x[0] for x in cave)

    for y in range(0, he + 1):
        print(f"{y:02}", end=" ")
        for x in range(ws, we + 1):
            if highlight is not None and highlight == (x, y):
                print("*", end="")
            else:
                if (x, y) in cave:
                    print(ROCK, end="")
                else:
                    print(".", end="")
        print()


def solve_one(data: str) -> Any:
    #     data = """498,4 -> 498,6 -> 496,6
    # 503,4 -> 502,4 -> 502,9 -> 494,9"""
    cave = {}
    for line in data.splitlines():
        rocks = [tuple(map(int, s.split(","))) for s in line.split(" -> ")]
        for start, end in sliding_window(rocks, 2):
            cave[start] = ROCK
            cave[end] = ROCK
            min_x = min(start[0], end[0])
            max_x = max(start[0], end[0])

            min_y = min(start[1], end[1])
            max_y = max(start[1], end[1])

            for i in range(min_x, max_x + 1):
                cave[(i, start[1])] = ROCK
            for i in range(min_y, max_y + 1):
                cave[(start[0], i)] = ROCK
    print_cave(list(cave.keys()))
    lowest_rock = max(x[1] for x in cave.keys())
    print("Lowest rock", lowest_rock)
    sand_total = 0
    while True:
        x, y = 500, 0
        # jump = min(s[1] for s in cave.keys() if s[0] == x) - 1
        # print("Jump to", jump)
        # y = jump
        while y < lowest_rock:
            if not cave.get((x, y + 1)):
                y += 1
            elif not cave.get((x - 1, y + 1)):
                x -= 1
                y += 1
            elif not cave.get((x + 1, y + 1)):
                x += 1
                y += 1
            else:
                cave[(x, y)] = SAND
                break
        else:

            break
        # print_cave(cave)
        sand_total += 1
    return sand_total


def solve_two(data: str) -> Any:
    #     data = """498,4 -> 498,6 -> 496,6
    # 503,4 -> 502,4 -> 502,9 -> 494,9"""
    cave = set()
    for line in data.splitlines():
        rocks = [tuple(map(int, s.split(","))) for s in line.split(" -> ")]
        for start, end in sliding_window(rocks, 2):
            print(f"{start} -> {end}")
            cave.add(start)
            cave.add(end)

            min_x = min(start[0], end[0])
            max_x = max(start[0], end[0])
            min_y = min(start[1], end[1])
            max_y = max(start[1], end[1])

            for i in range(min_x, max_x + 1):
                cave.add((i, start[1]))
            for i in range(min_y, max_y + 1):
                cave.add((start[0], i))

    lowest_rock = max(x[1] for x in cave) + 2
    print("Lowest rock", lowest_rock)
    minx, maxx = min(g[0] for g in cave), max(g[0] for g in cave)

    print_cave(list(cave))
    sand_total = 0
    falling = True
    while falling:
        x = 500
        y = 0
        while True:
            if y + 1 < lowest_rock:
                if not (x, y + 1) in cave:
                    y += 1
                    continue
                if not (x - 1, y + 1) in cave:
                    x -= 1
                    y += 1
                    continue
                if not (x + 1, y + 1) in cave:
                    x += 1
                    y += 1
                    continue
            if y == 0:
                falling = False
                break
            cave.add((x, y))
            sand_total += 1
            break
        # print_cave(cave)
        # Too high! 25501

    return sand_total + 1


def main(quiet: bool = False) -> None:
    run(DAY, 1, solve_one, quiet=quiet)
    run(DAY, 2, solve_two, quiet=quiet)


if __name__ == "__main__":
    main()
