from models.calc import Calc


def get_difficulty() -> int:
    while True:
        try:
            difficulty = int(
                input("Please specify the difficulty level [1, 2, 3 or 4]: ")
            )

            if difficulty in (1, 2, 3, 4):
                return difficulty

            print("Invalid difficulty. Choose between 1 and 4.")

        except ValueError:
            print("Please enter a valid number.")


def get_answer() -> int:
    while True:
        try:
            return int(input("Answer: "))
        except ValueError:
            print("Please enter a valid number.")


def wants_to_continue() -> bool:
    while True:
        try:
            option = int(input("Do you want to continue? [1 - Yes, 0 - No]: "))

            if option in (0, 1):
                return option == 1

            print("Choose 1 or 0.")

        except ValueError:
            print("Please enter a valid number.")


def play() -> None:
    points = 0

    while True:
        difficulty = get_difficulty()

        calc = Calc(difficulty)

        print("\nSolve the following operation:")
        calc.show_operation()

        answer = get_answer()

        if calc.check_answer(answer):
            points += 1
            print(f"Correct! You have {points} point(s).")
        else:
            print(f"Wrong! The correct answer was {calc.result}.")

        if not wants_to_continue():
            break

        print()

    print("\nThanks for playing!")
    print(f"Final score: {points} point(s).")
    print("See you next time!")


def main() -> None:
    play()


if __name__ == "__main__":
    main()
