from pathlib import Path
from typing import Callable, List
from time import perf_counter
import requests as requests
from rich.console import Console

console = Console()

YEAR = 2022
SESSION: str = Path(".session").read_text()


class timer:
    """from https://stackoverflow.com/a/69156219"""

    def __enter__(self):
        self.time = perf_counter()
        return self

    def __exit__(self, type, value, traceback):
        self.time = perf_counter() - self.time
        self.readout = f"{'':<4}Time: {self.time:.3f} seconds"
        print(self.readout)


def get_input(day: int) -> str:
    """inspired by https://github.com/alvesvaren/AoC-template/blob/main/aoc/_api.py"""
    Path("data").mkdir(exist_ok=True)
    f = Path(f"data/day_{day:02}.txt")
    if f.exists():
        return f.read_text()
    response = requests.get(
        f"https://adventofcode.com/{YEAR}/day/{day}/input", cookies={"session": SESSION}
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


def run(day: int, part: int, solver: Callable) -> None:
    data = get_input(day)
    console.print(f"=== RUNNING DAY {day} PART {part} ===", style="bold")
    with timer():
        solution = solver(data)
        console.print(f"{'':<4}ANSWER: [green]{solution}")
    print()
