#!/usr/bin/env python
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Callable, List, Any
from time import perf_counter
import requests as requests
import typer
from rich.console import Console

console = Console()

YEAR = 2022


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
        self.readout = f"{'':<4}Time: {self.time:.6f} seconds"
        print(self.readout)


def get_input(day: int) -> str:
    """inspired by https://github.com/alvesvaren/AoC-template/blob/main/aoc/_api.py"""
    Path("data").mkdir(exist_ok=True)
    f = Path(f"data/day_{day:02}.txt")
    if f.exists():
        return f.read_text()
    session: str = Path(".session").read_text()
    response = requests.get(
        f"https://adventofcode.com/{YEAR}/day/{day}/input", cookies={"session": session}
    )
    if not response.ok:
        if response.status_code == 404:
            raise FileNotFoundError(response.text)
        raise RuntimeError(
            f"Request failed, code: {response.status_code}, message: {response.content}"
        )
    data = response.text[:-1]
    f.write_text(data)
    return data


def wait_for_it(day: int) -> None:
    if days_since_dec1() < day:
        print("Blocking until puzzle unlocks")
        while days_since_dec1() < day:
            time.sleep(1)


def run(day: int, part: int, solver: Callable[[str], Any]) -> None:
    wait_for_it(day)
    data = get_input(day)
    console.print(f"=== RUNNING DAY {day} PART {part} ===", style="bold")
    with timer():
        solution = solver(data)
        console.print(f"{'':<6}ANSWER: [green]{solution}")
    print()


app = typer.Typer()


@app.command(name="gen")
def gen(day: int) -> None:
    template = Path("template.py.txt").read_text()
    data = template.replace("%DAY%", str(day))
    Path(f"day_{day:02}.py").write_text(data)


if __name__ == "__main__":
    app()
