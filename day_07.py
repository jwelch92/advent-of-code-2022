import time
from collections import Counter
from random import randint
from typing import Any, Text

import rich

from lib import run
from rich.console import Console
from rich.live import Live
from rich.tree import Tree
from rich.console import Group


DAY = 7


def anim(data: str) -> Any:
    console = Console()
    t = Tree("", highlight=True, hide_root=True)

    with Live(
        t, auto_refresh=False, vertical_overflow="visible", console=console
    ) as live:
        cur = t
        s = []
        for line in data.splitlines():
            sleep = 0.06
            match line.split():
                case ["$", "cd", target]:
                    instruction = Text(f"[bold]{line}")
                    # move up one
                    if target == "..":
                        s.pop()
                        cur = s[-1]
                    else:
                        cur = cur.add(
                            target,
                            highlight=True,
                            guide_style=f"color({randint(16, 255)})",
                        )
                        s.append(cur)
                    sleep = 0.2
                case ["$", "ls"]:
                    instruction = Text(f"[bold]{line}")
                case ["dir", dir]:
                    cur.add(f":open_file_folder: {dir}")
                    live.update(Group(instruction, cur), refresh=True)
                case [size, filename] if size.isdigit():
                    # Update the sizes for everything in the current tree
                    cur.add(f"📄 {filename} {size}")
                    live.update(Group(instruction, cur), refresh=True)
            time.sleep(sleep)
            live.update(Group(instruction, cur), refresh=True)

    rich.print(t)


def solve_one(data: str) -> Any:
    c = Counter()
    pwd = [""]
    for line in data.splitlines():
        # parsing using match just because
        match line.split():
            case ["$", "cd", target]:
                # move up one
                if target == "..":
                    pwd.pop()
                else:
                    # move down one
                    # This is kinda gross, the keys are weird
                    # ["", "//foo", "//foo/bar"]
                    # I could not figure out how to have it only keep 1 slash in the path, but it works nonetheless
                    pwd.append(f"{pwd[-1]}/{target}")
            case [size, _] if size.isdigit():
                # Update the sizes for everything in the current tree
                c.update({p: int(size) for p in pwd})
    # return the sum of all dirs that are greater than 100_000
    return sum(i for i in c.values() if i <= 100_000)


def solve_two(data: str) -> Any:
    DISK = 70_000_000
    NEED = 30_000_000
    DELTA = DISK - NEED
    c = Counter()
    pwd = [""]
    # Same as part 1
    for line in data.splitlines():
        match line.split():
            case ["$", "cd", target]:
                if target == "..":
                    pwd.pop()
                else:
                    pwd.append(f"{pwd[-1]}/{target}")
            case [size, _] if size.isdigit():
                c.update({p: int(size) for p in pwd})
            case _:
                pass
    # get the size of the root
    # Subtract how much space needs to be cleared
    threshold = c.most_common(1)[0][1] - DELTA
    # Get the smallest dir that's larger than the threshold
    return min(i for i in c.values() if i > threshold)


def main() -> None:
    # run(DAY, 1, solve_one)
    # run(DAY, 2, solve_two)
    run(DAY, 1, anim, quiet=True)


if __name__ == "__main__":
    main()
