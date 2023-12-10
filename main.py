import random

print(""" 
* Enter the number of times to roll the dice.
* Displays the value of each roll, and the total.
* Type 'exit' to quit.
""")


def roll_dice(number_of_rolls: int = 2) -> list[int]:
    """Rolls the dice and returns the result as a list.

    Args:
        number_of_rolls (int, optional): The number of times to roll the dice. Defaults to 2.

    Returns:
        list[int]: A list of dice rolls.
    """
    if number_of_rolls <= 0:
        raise ValueError

    rolls: list[int] = []
    for i in range(number_of_rolls):
        random_roll: int = random.randint(1, 6)
        rolls.append(random_roll)

    return rolls


def main():
    while True:
        try:
            user_input: str = input("How many dice would you like to roll? ")

            if user_input.lower() == "exit":
                print("Thanks for playing!")
                break

            dice_rolls: list[int] = roll_dice(int(user_input))
            print(*dice_rolls, "(" + str(sum(dice_rolls)) + ")", sep=", ")
        except ValueError:
            print("(Please enter a valid number.)")


if __name__ == "__main__":
    main()
