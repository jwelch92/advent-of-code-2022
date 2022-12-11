import math
from collections import deque
from dataclasses import dataclass
from functools import reduce, cache
from operator import mul
from typing import Any

from lib import run


# AOC DAY 11


@dataclass()
class Monkey:
    items: deque[int]
    id: int
    op: str
    test: int
    jump_true: int
    jump_false: int

    p: int = 0


DAY = 11


def parse_data(data: str) -> list[Monkey]:
    monkeys = []
    for monkey in data.split("\n\n"):
        for line in monkey.splitlines():
            instruction = [x.strip() for x in line.strip().split(":")]
            match instruction:
                case [monkey_id, ""]:
                    id = int(monkey_id.split(" ")[-1])
                case ["Starting items", _items]:
                    items = deque([int(c) for c in _items.split(",")])
                case ["Operation", op]:
                    pass
                case ["Test", _test]:
                    test = int(_test.split(" ")[-1])
                case ["If true", t]:
                    jump_true = int(t.split(" ")[-1])
                case ["If false", f]:
                    jump_false = int(f.split(" ")[-1])

        monkeys.append(
            Monkey(
                id=id,
                items=items,
                op=op,
                test=test,
                jump_true=jump_true,
                jump_false=jump_false,
            )
        )
    return monkeys


@cache
def _eval_op(op, old) -> int:
    op = op.split(" = ")[-1]
    return eval(op, {"old": old})


def solve_one(data: str) -> Any:
    print(data)
    monkeys = parse_data(data)
    for round in range(20):
        print(f"===== ROUND: {round} ======")
        print(monkeys)
        for monkey in monkeys:
            while len(monkey.items):
                monkey.p += 1
                worry = monkey.items.popleft()
                print(f"processing {worry=} for monkey {monkey.id}")
                worry = _eval_op(monkey.op, worry)
                worry = math.floor(worry / 3)
                if worry % monkey.test == 0:
                    monkeys[monkey.jump_true].items.append(worry)
                else:
                    monkeys[monkey.jump_false].items.append(worry)
    inspected = sorted([m.p for m in monkeys])
    return inspected[-1] * inspected[-2]


def solve_two(data: str) -> Any:
    monkeys = parse_data(data)
    prod = reduce(mul, [m.test for m in monkeys])
    for round in range(10_000):
        for monkey in monkeys:
            while len(monkey.items):
                monkey.p += 1
                worry = monkey.items.popleft()
                worry = _eval_op(monkey.op, worry) % prod
                if worry % monkey.test == 0:
                    monkeys[monkey.jump_true].items.append(worry)
                else:
                    monkeys[monkey.jump_false].items.append(worry)
    inspected = sorted([m.p for m in monkeys])
    score = reduce(mul, inspected[-2:])
    return score


def main(quiet: bool = False) -> None:
    run(DAY, 1, solve_one, quiet=quiet)
    run(DAY, 2, solve_two, quiet=quiet)


if __name__ == "__main__":
    main()
