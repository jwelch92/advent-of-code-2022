import bisect
import functools
import queue
import string
from collections import defaultdict
from dataclasses import dataclass, field
from pprint import pprint

from lib import run
from typing import Any

# AOC DAY 12


DAY = 12

Coord = tuple[int, int]


@dataclass()
class Node:
    coord: Coord = field(compare=False)
    previous: list[Coord] = field(compare=False)
    path_cost: int = field(default=0)
    heuristic_cost: int = field(default=0)

    def cost(self) -> int:
        return self.path_cost + self.heuristic_cost

    def previous_inclusive(self) -> list[Coord]:
        return self.previous + [self.coord]

    def __eq__(self, other) -> bool:
        return self.coord == other.coord

    def __lt__(self, other):
        return self.cost() < other.cost()

    def __hash__(self):
        return hash(self.coord)


directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def neighbors(c: Coord, width: int, height: int) -> list[Coord]:
    coords = []
    for (dx, dy) in directions:
        x, y = c
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= width or ny < 0 or ny >= height:
            continue
        coords.append((nx, ny))
    return coords


def solve_one(data: str) -> Any:
    #     data = """Sabqponm
    # abcryxxl
    # accszExk
    # acctuvwj
    # abdefghi"""
    grid = []
    start_x, start_y = 0, 0
    end_x, end_y = 0, 0
    for y, line in enumerate(data.splitlines()):
        row = []
        for x, c in enumerate(line):
            if c == "S":
                row.append(ord("a"))
                start_x, start_y = x, y
            elif c == "E":
                row.append(ord("z"))
                end_x, end_y = x, y
            else:
                row.append(ord(c))
        grid.append(row)

    width = len(grid[0])
    height = len(grid)

    get_neighbors = functools.partial(neighbors, width=width, height=height)

    def heuristic(x: int, y: int) -> int:
        # Try by actually walking the x, y distance and taking mean of scores?
        return abs(end_x - x) + abs(end_y - y)

    moves = """v..v<<<<
>v.vv<<^
.>vv>E^^
..v>>>^^
..>>>>>^"""

    coords = []
    for y, line in enumerate(moves.splitlines()):
        for x, c in enumerate(line):
            if c != ".":
                coords.append((x, y))
    pprint(coords)

    print("\n".join("".join(str(r)) for r in grid))
    # BFS
    # default value for path is very high so new coords are always searched
    path = defaultdict(lambda: 10e14)
    path[(start_y, start_x)] = 0
    search = [(start_x, start_y, 0)]

    while len(search) > 0:
        x, y, steps = search.pop(0)
        from_elevation = grid[y][x]
        cells = get_neighbors((x, y))
        for (nx, ny) in cells:
            to_elevation = grid[ny][nx]
            # Can only move up 1 level but down any
            if not from_elevation - to_elevation >= -1:
                continue
            if path[(ny, nx)] > steps + 1:
                path[(ny, nx)] = steps + 1
                search.append((nx, ny, steps + 1))

    return path[(end_y, end_x)]

    #
    # start = Node(
    #         coord=(start_x, start_y),
    #         previous=list(),
    #         path_cost=0,
    #         heuristic_cost=heuristic(start_x, start_y),
    #     )
    # fringe: list[Node] = [
    #     start
    # ]
    #
    # openpath: dict[Coord, Node] = {start.coord: start}
    # closepath: dict[Coord, int] = {}
    #
    # # compare
    # print(start_x, start_y)
    # print(end_x, end_y)
    #
    # print(grid)
    # path: list = []
    # print("Starting!")
    # while len(fringe) > 0:
    #     state = fringe.pop()
    #     openpath.pop(state.coord)
    #     if state.coord in closepath:
    #         continue
    #
    #     print("visiting", state.coord)
    #     x, y = state.coord
    #     if grid[y][x] == 27:
    #         print("FOUND!")
    #         path = state.previous + [state.coord]
    #         path.reverse()
    #         print(path)
    #         print(len(path))
    #         break
    #
    #     closepath[(x, y)] = state.cost()
    #
    #     neighbors = []
    #     # Up
    #     cur_elevation = grid[y][x]
    #     # not from_elevation - to_elevation >= -1
    #     if y > 0 and cur_elevation - grid[y - 1][x] >= -1:
    #         neighbors.append((x, y - 1))
    #     # Down
    #     if y < height - 1 and cur_elevation - grid[y + 1][x] >= -1:
    #         neighbors.append((x, y + 1))
    #
    #     # Left
    #     if x > 0 and cur_elevation - grid[y][x - 1] >= -1:
    #         neighbors.append((x - 1, y))
    #     # Right
    #     if x < width - 1 and cur_elevation - grid[y][x + 1] >= -1:
    #         neighbors.append((x + 1, y))
    #
    #     print("neighbors", neighbors)
    #
    #     for n in neighbors:
    #         n_x, n_y = n
    #         next_cost = state.path_cost + 1
    #         print("next cost", next_cost)
    #         if n in closepath:
    #             continue
    #
    #         child = Node(
    #                 coord=n,
    #                 previous=state.previous_inclusive(),
    #                 path_cost=next_cost,
    #                 heuristic_cost=heuristic(*n),
    #             )
    #         dupe = openpath.get(child.coord)
    #         if not dupe:
    #             openpath[child.coord] = child
    #             bisect.insort_left(fringe, child)
    #         else:
    #             l = bisect.bisect_left(fringe, dupe)
    #             r = bisect.bisect_right(fringe, dupe)
    #             fringe.pop((fringe.index(dupe, l, r)))
    #             openpath[child.coord] = child
    #             bisect.insort_left(fringe, child)
    #
    #
    #     fringe.sort(key=lambda n: n.cost())
    #
    # print(sorted(coords))
    # print(sorted(path))
    # print(list(set(coords).difference(set(path))))
    #
    # return len(path) - 1


def solve_two(data: str) -> Any:
    #     data = """Sabqponm
    # abcryxxl
    # accszExk
    # acctuvwj
    # abdefghi"""
    grid = []
    start_x, start_y = 0, 0
    end_x, end_y = 0, 0
    for y, line in enumerate(data.splitlines()):
        row = []
        for x, c in enumerate(line):
            if c == "S":
                row.append(ord("a"))
                start_x, start_y = x, y
            elif c == "E":
                row.append(ord("z"))
                end_x, end_y = x, y
            else:
                row.append(ord(c))
        grid.append(row)

    width = len(grid[0])
    height = len(grid)

    get_neighbors = functools.partial(neighbors, width=width, height=height)

    # Start at the end
    path = defaultdict(lambda: 10e14)
    path[(end_y, end_x)] = 0
    search = [(end_x, end_y, 0)]

    while len(search) > 0:
        x, y, steps = search.pop(0)

        from_elevation = grid[y][x]
        cells = get_neighbors((x, y))
        for (nx, ny) in cells:
            to_elevation = grid[ny][nx]
            # From end to start means we can only go down 1 level at a time but up any number
            if not from_elevation - to_elevation <= 1:
                continue

            if path[(ny, nx)] > steps + 1:
                path[(ny, nx)] = steps + 1
                search.append((nx, ny, steps + 1))
    # Get the smallest distance value from all points where elevation is 'a'
    shortest = min([d for ((y, x), d) in path.items() if grid[y][x] == ord("a")])
    return shortest


def main(quiet: bool = False) -> None:
    run(DAY, 1, solve_one, quiet=quiet)
    run(DAY, 2, solve_two, quiet=quiet)


if __name__ == "__main__":
    main()
