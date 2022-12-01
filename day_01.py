from lib import run


def solve_one(data: str) -> int:
    return 2


def solve_two(data: str) -> int:
    return 1231

# TODO templatize this
def main() -> None:
    run(1, 1, solve_one)
    run(1, 2, solve_two)

if __name__ == "__main__":
    main()
