from typing import Any

from lib import run

# AOC DAY 10


DAY = 10

DATA = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""


def solve_one(data: str) -> Any:
    # data = DATA
    signal = 0
    cycle = 1
    X = 1
    program = data.splitlines()

    for line in program:
        instruction = line.split()
        for i in range(2 if "addx" in instruction else 1):
            # cycle count for instructions
            # If we're at 20 or 40th then measure signal
            if (cycle - 20) % 40 == 0:
                signal += cycle * X
            cycle += 1
        # complete instruction
        if "addx" in instruction:
            X += int(instruction[1])

    return signal


def solve_two(data: str) -> Any:
    signal = 0
    cycle = 1
    X = 1
    program = data.splitlines()

    for line in program:
        instruction = line.split()
        for i in range(2 if "addx" in instruction else 1):
            pixel = (cycle - 1) % 40  # 40 pixels wide, 0-39
            char = "█" if abs(X - pixel) <= 1 else "."  # draw a █ if the sprite covers the current pixel. The sprite is 3 wide, so we check if the position is within 1 on either side
            endl = "\n" if pixel == 39 else "" # Print newline to move to the next row of pixels when we've hit the end (pixel 39)
            print(char, end=endl)
            cycle += 1
        # complete the addx instruction
        if "addx" in instruction:
            X += int(instruction[1])

    return signal


def main(quiet: bool = False) -> None:
    run(DAY, 1, solve_one, quiet=quiet)
    run(DAY, 2, solve_two, quiet=quiet)


if __name__ == "__main__":
    main()
