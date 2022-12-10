import copy
import sys
import time
from dataclasses import dataclass
from pprint import pprint
import math

import pygame
from rich.live import Live

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


def render(rope: list[tuple[int, int]], grid_x: int, grid_y: int) -> str:
    # width = max(x[1] for x in rope)
    # height = max(x[0] for x in rope)

    grid = []
    for r in range(~(grid_y // 2), grid_y // 2):

        line = []
        for c in range(~(grid_x // 2), grid_x // 2):
            # print(f"Checking ({c}, {r})")
            if (c, r) in rope:
                print("Found coord!")
                line.append(str(rope.index((c, r))))
            else:
                line.append(".")
        grid.append(line)

    return "\n".join(["".join(l) for l in reversed(grid)])


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
                        t[0] + dx,
                        t[1] + dy
                    )
                visited.add(rope[-1])

    return len(visited)


def anim(data: str) -> Any:
    visited = set()
    frames = []
    rope = [(200, 200) for _ in range(10)]

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
            frames.append(copy.deepcopy(rope))
            for i in range(1, len(rope)):
                h = rope[i - 1]
                t = rope[i]
                d = delta(h, t)
                if abs(d[0]) > 1 or abs(d[1]) > 1:
                    dx = 0 if d[0] == 0 else 1 if d[0] > 0 else -1
                    dy = 0 if d[1] == 0 else 1 if d[1] > 0 else -1
                    rope[i] = (
                        t[0] + dx,
                        t[1] + dy
                    )
                    frames.append(copy.deepcopy(rope))
                visited.add(rope[-1])

    # min_x = min(min(x[0] for x in rope) for rope in frames)
    # min_y = min(min(x[1] for x in rope) for rope in frames)
    # max_x = max(max(x[0] for x in rope) for rope in frames)
    # max_y = max(max(x[1] for x in rope) for rope in frames)
    # round_10 = lambda n: math.ceil(n / 10) * 10
    # grid_x = round_10(abs(max_x - min_x))
    # grid_y = round_10(abs(max_y - min_y))
    # print(grid_x, grid_y)
    #
    # print("X", min_x, max_x)
    # print("Y", min_y, max_y)
    #
    # # print(frames)
    #
    # with Live(render(frames[0], grid_x=grid_x, grid_y=grid_y), auto_refresh=False, screen=True) as live:
    #     for f in frames:
    #         live.update(render(f, grid_x=grid_x, grid_y=grid_y), refresh=True)
            # time.sleep(0.001)
    # print(render(frames[35], grid_x=grid_x, grid_y=grid_y))

    # Window size
    window_x = 720
    window_y = 480

    # defining colors
    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    blue = pygame.Color(0, 0, 255)

    # Initialising pygame
    pygame.init()

    # Initialise game window
    pygame.display.set_caption('Advent of Code Day 9')
    game_window = pygame.display.set_mode((window_x, window_y))
    fps_controller = pygame.time.Clock()




    for frame in frames:
        game_window.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for pos in frame:
            pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.display.update()
        # Refresh rate
        fps_controller.tick(25)


    return len(visited)


def main(quiet: bool = False) -> None:
    # run(DAY, 1, solve_one, quiet=quiet)
    # run(DAY, 2, solve_two, quiet=quiet)
    run(DAY, 1, anim, quiet=True)


if __name__ == "__main__":
    main()
