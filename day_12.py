from collections import defaultdict
from pprint import pprint
from typing import Any

from lib import run, neighbors_fn, build_grid

# AOC DAY 12


DAY = 12


def solve_one(data: str) -> Any:
    #     data = """Sabqponm
    # abcryxxl
    # accszExk
    # acctuvwj
    # abdefghi"""
    grid, height, width, points, values = build_grid(data, cast_fn=lambda x: ord(x))
    start_x, start_y = values[ord("S")][0]
    grid[start_y][start_x] = ord("a")
    end_x, end_y = values[ord("E")][0]
    grid[end_y][end_x] = ord("z")

    get_neighbors = neighbors_fn(width, height)

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


def solve_two(data: str) -> Any:
    #     data = """Sabqponm
    # abcryxxl
    # accszExk
    # acctuvwj
    # abdefghi"""
    grid, height, width, points, values = build_grid(data, cast_fn=lambda x: ord(x))
    get_neighbors = neighbors_fn(width, height)
    start_x, start_y = values[ord("S")][0]
    grid[start_y][start_x] = ord("a")
    end_x, end_y = values[ord("E")][0]
    grid[end_y][end_x] = ord("z")

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
