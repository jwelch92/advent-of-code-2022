import re
from typing import Any

from lib import run

# AOC DAY 16


DAY = 16

TEST_DATA = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""


def solve_one(data: str) -> Any:
    # I think this can be done with BFS?
    # There's something about Floyd-Warshall I keep seeing. Then use DFS???
    pat = re.compile(r"Valve ([A-Z]{2}).*rate=(\d+);.*valves? (.*)$", re.MULTILINE)
    m = pat.findall(data)

    flow_rates: dict[str, int] = {}
    tunnels: dict[str, list[str]] = {}
    opened: set[str] = set()

    for v, flow_rate, n in m:
        neighbors = n.replace(" ", "").split(",")
        flow_rates[v] = int(flow_rate)
        tunnels[v] = neighbors

    max_pressure = -1

    def walk(
        time: int, position: str, rates: list[int], seen: dict[tuple[int, str], int]
    ):
        print("visting", position)
        if seen.get((time, position), -1) >= sum(rates):
            return
        seen[(time, position)] = sum(rates)
        if time == 30:
            s = sum(rates)
            print(s)
            nonlocal max_pressure
            if s > max_pressure:
                max_pressure = s
            return s

        for i in (0, 1):
            if i == 0:
                if position in opened or flow_rates[position] <= 0:
                    continue
                opened.add(position)
                running_rate_total = sum(flow_rates[k] for k in opened)
                walk(time + 1, position, rates + [running_rate_total], seen)
                opened.remove(position)
            else:
                running_rate_total = sum(flow_rates[k] for k in opened)
                for tun in tunnels[position]:
                    walk(time + 1, tun, rates + [running_rate_total], seen)

    print(walk(1, "AA", [0], dict()))
    print(max_pressure)


def solve_two(data: str) -> Any:
    pass


def main(quiet: bool = False) -> None:
    run(DAY, 1, solve_one, quiet=quiet)
    run(DAY, 2, solve_two, quiet=quiet)


if __name__ == "__main__":
    main()
