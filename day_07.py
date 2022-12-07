from collections import Counter
from typing import Any

from lib import run

# AOC DAY 7


DAY = 7


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
    run(DAY, 1, solve_one)
    run(DAY, 2, solve_two)


if __name__ == "__main__":
    main()
