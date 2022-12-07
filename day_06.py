import time
from collections import deque
from typing import Any

from more_itertools import sliding_window
from rich.console import Console
from rich.live import Live
from rich.text import Text

from lib import run, get_input

# AOC DAY 6


DAY = 6


def solve_one(data: str) -> Any:
    return (
        next(
            (
                data.index("".join(c))
                for c in sliding_window(data, 4)
                if len(set(c)) == 4
            )
        )
        + 4
    )


def solve_two(data: str) -> Any:
    return (
        next(
            (
                data.index("".join(c))
                for c in sliding_window(data, 14)
                if len(set(c)) == 14
            )
        )
        + 14
    )


def anim(data: str) -> Any:
    console = Console()
    b = deque()
    answer = 0
    part = 14
    with Live(Text(data), auto_refresh=False, console=console, screen=True) as live:
        for i, c in enumerate(data):
            time.sleep(0.005)
            live.update(
                Text.assemble(
                    (data[: i - part - 1], "dim red"),
                    ("[[[" + data[i - part : i] + "]]]", "bold cyan"),
                    data[i:],
                ),
                refresh=True,
            )
            if len(b) == part:
                if len(set(b)) == part and i > 4:
                    live.update(
                        Text.assemble(
                            (data[: i - part - 1], "dim red"),
                            ("[[[" + data[i - part : i] + "]]]", "bold cyan"),
                            (data[i:], "green"),
                        ),
                        refresh=True,
                    )
                    answer = i
                    break
                b.popleft()
            b.append(c)
        for i in range(5):
            live.update(
                Text.assemble(
                    (data[: answer - 3], "dim red"),
                    ("[[[" + data[answer - part : answer] + "]]]", "bold cyan"),
                    (data[answer:], f"{'bold' if i % 2 == 0 else 'dim'} green"),
                ),
                refresh=True,
            )
            time.sleep(0.3)
        time.sleep(5)
    console.print(f"[bold blue]Index of start-of-packet marker: {answer}")
    return answer


def main() -> None:
    # run(DAY, 1, solve_one)
    # run(DAY, 2, solve_two)
    anim(get_input(DAY))


if __name__ == "__main__":
    main()
