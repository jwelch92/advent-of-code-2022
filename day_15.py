import math
import re

from lib import run
from typing import Any

# AOC DAY 15

DAY = 15


TEST_DATA = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""


def solve_one(data: str) -> Any:
    # data = TEST_DATA
    scan_row = 2_000_000
    # cave = {}
    sensor_data = []
    for line in data.splitlines():
        sx, sy, bx, by = [int(x) for x in re.findall(r"[x|y]=(-?\d+)", line)]
        sensor_data.append((sx, sy, abs(sx - bx) + abs(sy - by)))
    print(sensor_data)
    high_x = -math.inf
    low_x = math.inf

    for sx, sy, md in sensor_data:
        d = md - abs(
            scan_row - sy
        )  # subtract the y part of the distance to get just the x component
        if d > 0:  # if gt 0 then this scan intersects by d blocks on either side of sx
            # Set the high x point
            high_x = max(high_x, sx + d)
            # set the low x
            low_x = min(low_x, sx - d)

    print(high_x - low_x)
    # Return the difference between the first and last block on the target row that have been scanned
    return high_x - low_x

    # check row y=10 for testing
    # check row y=2_000_000 for real


def score(x, y, factor=4000000) -> int:
    """
    To isolate the distress beacon's signal,
    you need to determine its tuning frequency,
    which can be found by multiplying its x coordinate by 4000000 and then adding its y coordinate.
    """
    return (x * factor) + y


def manhattan(a, b) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def solve_two(data: str) -> Any:
    # data = TEST_DATA
    max_search = 4000000

    sensor_data = []
    for line in data.splitlines():
        sx, sy, bx, by = [int(x) for x in re.findall(r"[x|y]=(-?\d+)", line)]
        sensor_data.append((sx, sy, abs(sx - bx) + abs(sy - by)))

    # For each sensor
    # Search along perimeter that is manhattan + 1
    # Look for a point that is within bounds AND is further away than all other beacons (larger manhattan with all sensors than known beacons)
    # > Find the only possible position for the distress beacon.
    # This should mean the point is unique so it must be somewhere within manhattan+1 of a sensor, otherwise it could just be anywhere
    # from z3 import Int, Solver, If
    # def z3abs(x):
    #     return If(x >= 0, x, -x)
    # # what the heck is this!
    # # It's so fast!
    # s = Solver()
    # x = Int("x")
    # y = Int("y")
    # s.add(x >= 0)
    # s.add(x <= 4000000)
    # s.add(y >= 0)
    # s.add(y <= 4000000)
    # for sx, sy, d in sensor_data:
    #     s.add(z3abs(x - sx) + z3abs(y - sy) > d)
    #
    # s.check()
    # model = s.model()
    # done = model[x].as_long() * 4000000 + model[y].as_long()
    # print(done)
    # return done

    for sx, sy, sd in sensor_data:
        for c in range(sd + 1):
            moves = [
                # sx - sd - 1 moves to the left-most point
                # the c incrementing value moves it left or right on each iteration
                # as y shifts too to "move" the scan along the outside perimeter of the diamond
                ((sx - sd - 1 + c), (sy - c)),  # left to top
                ((sx + sd + 1 - c), (sy - c)),  # right to top
                ((sx - sd - 1 + c), (sy + c)),  # left to bottom
                ((sx + sd + 1 - c), (sy + c)),  # right to bottom
            ]
            for dx, dy in moves:
                if 0 <= dx <= max_search and 0 <= dy <= max_search:
                    # the manhattan for this point must be greater than all known beacons
                    if all([abs(dx - x) + abs(dy - y) > d for x, y, d in sensor_data]):
                        # score it accordingly
                        return score(dx, dy)


def main(quiet: bool = False) -> None:
    run(DAY, 1, solve_one, quiet=quiet)
    run(DAY, 2, solve_two, quiet=quiet)


if __name__ == "__main__":
    main()
