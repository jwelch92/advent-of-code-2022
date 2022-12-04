from lib import run

# AOC DAY 4


def solve_one(data: str) -> int:
    answer = 0
    for line in data.splitlines():
        a, b = line.split(",")
        a1, a2 = (int(i) for i in a.split("-"))
        b1, b2 = (int(i) for i in b.split("-"))
        if a2 - a1 > b2 - b1:
            # a is bigger
            if b1 >= a1 and b2 <= a2:
                answer += 1
        else:
            # b is bigger range
            if a1 >= b1 and a2 <= b2:
                answer += 1
    return answer


def solve_two(data: str) -> int:
    answer = 0
    for line in data.splitlines():
        a, b = line.split(",")
        a1, a2 = (int(i) for i in a.split("-"))
        s_a = set(range(a1, a2+1))
        b1, b2 = (int(i) for i in b.split("-"))
        s_b = set(range(b1, b2 + 1))
        if s_a.intersection(s_b):
            answer += 1

    return answer



def main() -> None:
    run(4, 1, solve_one)
    run(4, 2, solve_two)


if __name__ == "__main__":
    main()
