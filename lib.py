#!/usr/bin/env python
import time
from collections import defaultdict
from datetime import datetime, timezone, timedelta
from functools import cache
from pathlib import Path
from typing import Callable, List, Any, Iterator, Iterable
from time import perf_counter
import requests as requests
import typer
from more_itertools import sliding_window
from rich.console import Console
from rich.status import Status

console = Console()

YEAR = 2022

Point = tuple[int, int]


def neighbors_fn(
    width: int, height: int, diag: bool = False
) -> Callable[[Point], Iterator[Point]]:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    if diag:
        directions.extend([(1, 1), (1, -1), (-1, 1), (-1, -1)])

    @cache
    def neighbors(point: Point) -> Iterator[Point]:
        for (dx, dy) in directions:
            x, y = point
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= width or ny < 0 or ny >= height:
                continue
            yield nx, ny

    return neighbors


GridCell = str | int | float
Grid = list[list[str | int | float]]
PointIndex = dict[Point, str | int | float]
ValueIndex = dict[str | int | float, list[Point]]

# TODO cast function
# TODO splitter function
def build_grid(
    data: str,
    cast_fn: Callable[[Any], str | int | float] | None = None,
    split_fn: Callable[[Iterable[Any]], Iterable[str | int | float]] | None = None,
) -> tuple[Grid, int, int, PointIndex, ValueIndex]:
    grid = []
    points = {}
    values = defaultdict(list)
    if cast_fn is None:
        cast_fn = lambda x: x
    if split_fn is None:
        split_fn = lambda xs: xs
    for y, row in enumerate(data.splitlines()):
        line = []
        for x, col in enumerate(split_fn(row)):  # TODO custom splitter
            col = cast_fn(col)
            line.append(col)
            points[(x, y)] = col
            values[col].append((x, y))
        grid.append(line)

    return grid, len(grid), len(grid[0]), points, values


def first_unique_sequence(data: str, length: int) -> int:
    """From day 6, finds the index of the start marker for a packet. The marker is the first index where the preceding 4 characters are unique."""
    return (
        next(
            (
                data.index("".join(c))
                for c in sliding_window(data, length)
                if len(set(c)) == length
            )
        )
        + length
    )


def days_since_dec1():
    # Create a datetime object for December 1, 2022, 12am ET
    target_datetime = datetime(
        2022, 12, 1, 0, 0, 0, tzinfo=timezone(-timedelta(hours=5))
    )
    current_datetime = datetime.now(timezone(-timedelta(hours=5)))
    difference = current_datetime - target_datetime
    return difference.days + 1


class timer:
    """from https://stackoverflow.com/a/69156219"""

    def __enter__(self):
        self.time = perf_counter()
        return self

    def __exit__(self, type, value, traceback):
        self.time = perf_counter() - self.time
        ms = self.time * 1000
        self.readout = f"{'':<4}Time: {ms:2f} ms"
        print(self.readout)


def get_input(day: int) -> str:
    """inspired by https://github.com/alvesvaren/AoC-template/blob/main/aoc/_api.py"""
    Path("data").mkdir(exist_ok=True)
    f = Path(f"data/day_{day:02}.txt")
    if f.exists():
        return f.read_text()
    session: str = Path(".session").read_text()
    response = requests.get(
        f"https://adventofcode.com/{YEAR}/day/{day}/input",
        cookies={"session": session},
        headers={
            "User-Agent": "https://github.com/jwelch92/advent-of-code-2022 by jwelch92@gmail.com",
            "From": "jwelch92@gmail.com",
        },
    )
    if not response.ok:
        if response.status_code == 404:
            raise FileNotFoundError(response.text)
        raise RuntimeError(
            f"Request failed, code: {response.status_code}, message: {response.content}"
        )
    data = response.text[:-1]
    f.write_text(data)
    print(data)
    return data


def wait_for_it(day: int) -> None:
    try:
        if days_since_dec1() < day:
            with Status("Blocking until puzzle unlocks"):
                while days_since_dec1() < day:
                    time.sleep(1)
    except Exception:
        pass


def run(day: int, part: int, solver: Callable[[str], Any], quiet: bool = False) -> None:
    wait_for_it(day)
    data = get_input(day)
    if not quiet:
        console.print(f"=== RUNNING DAY {day} PART {part} ===", style="bold")
    with timer():
        solution = solver(data)
        if not quiet:
            console.print(f"{'':<6}ANSWER: [green]{solution}")
    if not quiet:
        print()


app = typer.Typer()


@app.command(name="gen")
def gen(day: int) -> None:
    template = Path("template.py.txt").read_text()
    data = template.replace("%DAY%", str(day))
    Path(f"day_{day:02}.py").write_text(data)


if __name__ == "__main__":
    app()
