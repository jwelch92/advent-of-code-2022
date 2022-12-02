from pprint import pprint

from lib import run

# AOC DAY 2

ROCK = 1
PAPER = 2
SCISSORS = 3

LOSS = 0
DRAW = 3
WIN = 6

MAP = {
    "X": "A",
    "Y": "B",
    "Z": "C"
}

SCORE_MAP = {
    "A": 1,
    "B": 2,
    "C": 3
}


def solve_one(data: str) -> int:
    rounds = data.splitlines()
    score = 0
    # pprint(rounds)
    for l in rounds:
        opp, you = l.split(" ")
        you = MAP[you]
        print(opp, you)
        if you == opp:
            score += (DRAW + SCORE_MAP[you])
        elif opp == "A":
            if you == "B":
                score += (WIN + SCORE_MAP[you])
            else:
                score += (LOSS + SCORE_MAP[you])
        elif opp == "B":
            if you == "C":
                score += (WIN + SCORE_MAP[you])
            else:
                score += (LOSS + SCORE_MAP[you])
        elif opp == "C":
            if you == "A":
                score += (WIN + SCORE_MAP[you])
            else:
                score += (LOSS + SCORE_MAP[you])

    return score



def solve_two(data: str) -> int:
    score = 0
    rounds = data.splitlines()
    for l in rounds:
        opp, you = l.split(" ")
        if you == "X":
            if opp == "A":
                score += (LOSS + SCISSORS)
            elif opp == "B":
                score += (LOSS + ROCK)
            else:
                score += (LOSS + PAPER)

        elif you == "Y":
            if opp == "A":
                score += (DRAW + ROCK)
            elif opp == "B":
                score += (DRAW + PAPER)
            else:
                score += (DRAW + SCISSORS)
        else:
            if opp == "A":
                score += (WIN + PAPER)
            elif opp == "B":
                score += (WIN + SCISSORS)
            else:
                score += (WIN + ROCK)

    return score
def main() -> None:
    run(2, 1, solve_one)
    run(2, 2, solve_two)


if __name__ == "__main__":
    main()
