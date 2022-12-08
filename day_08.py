import itertools
from pprint import pprint

from lib import run
from typing import Any, List

# AOC DAY 8


DAY = 8


def pt(tree):
    for line in tree:
        print("".join((str(i) for i in line)))


def solve_one(data: str) -> Any:
    forest = []
    for line in data.splitlines():
        forest.append([int(i) for i in line])
    # after several tries I went back to the drawing board and finally got this working in a nice way
    # I tried lots of stuff
    # Looped-ish versions of this but I got confused with keeping track of indexes and stuff
    # Tried some fancy scanning or searching based of the max in a row
    # Tried some matrix stuff. Transpose to do searches on rows only and avoid nested loops
    # I think there's probably some binary search split based on the max in a slice that could work well
    visible = 0
    for y, row in enumerate(forest):
        for x, col in enumerate(row):
            tree = forest[y][x]
            top = [tree > r[x] for r in forest[:y]]
            bottom = [tree > r[x] for r in forest[y + 1 :]]
            left = [tree > col for col in forest[y][:x]]
            right = [tree > col for col in forest[y][x + 1 :]]

            if any(map(all, [top, bottom, left, right])):
                visible += 1

    return visible


def solve_two(data: str) -> Any:
    forest = []
    for line in data.splitlines():
        forest.append([int(i) for i in line])
    # Part two is looking for scenic views
    # This solution already has a list that is basically all of the viewable trees until an edge or a taller tree

    # [True, True, True, False] means that there are 3 trees visible
    scenic = []

    def visible(survey: List[bool]) -> int:
        # Check if the survey results have a taller tree
        return survey.index(False) + 1 if False in survey else len(survey)

    for y, row in enumerate(forest):
        for x, col in enumerate(row):
            tree = forest[y][x]
            # Creates a "survey" which is a list of bools. Any False means a taller tree was found
            # Scan this column from the top down looking for any trees taller than current
            top = list(
                reversed([tree > r[x] for r in forest[:y]])
            )  # iterates "backwards" for this part
            # Scan this column from the current row down looking for any trees taller than current
            bottom = [tree > r[x] for r in forest[y + 1 :]]
            # Scan this row from the beginning to find taller trees
            left = list(
                reversed([tree > col for col in forest[y][:x]])
            )  # iterates "backwards" for this part
            # Scan this row from the current column to find higher trees
            right = [tree > col for col in forest[y][x + 1 :]]
            # Score this tree
            visible_top = visible(top)
            visible_bottom = visible(bottom)
            visible_left = visible(left)
            visible_right = visible(right)
            score = visible_top * visible_bottom * visible_left * visible_right
            scenic.append(score)

    return max(scenic)


def main() -> None:
    run(DAY, 1, solve_one)
    run(DAY, 2, solve_two)


if __name__ == "__main__":
    main()
