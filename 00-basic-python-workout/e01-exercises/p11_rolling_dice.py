from random import randint


def roll_dice():
    dice_faces = {
        1: [
            "┌───────┐",
            "│   1   │",
            "│   ●   │",
            "│       │",
            "└───────┘"
        ],
        2: [
            "┌───────┐",
            "│ ●     │",
            "│   2   │",
            "│     ● │",
            "└───────┘"
        ],
        3: [
            "┌───────┐",
            "│ ● 3   │",
            "│   ●   │",
            "│     ● │",
            "└───────┘"
        ],
        4: [
            "┌───────┐",
            "│ ●   ● │",
            "│   4   │",
            "│ ●   ● │",
            "└───────┘"
        ],
        5: [
            "┌───────┐",
            "│ ●   ● │",
            "│   ●   │",
            "│ ● 5 ● │",
            "└───────┘"
        ],
        6: [
            "┌───────┐",
            "│ ●   ● │",
            "│ ● 6 ● │",
            "│ ●   ● │",
            "└───────┘"
        ],
    }

    freq_map_dice_roll = {i: 0 for i in range(1, 7)}
    freq_map_rolls = {i: 0 for i in range(2, 13)}

    done = False
    while not done:
        should_roll_dice = input("Roll the dice? (Yes/No): ")
        if should_roll_dice.lower() == "Yes".lower():
            roll_1 = randint(1, 6)
            roll_2 = randint(1, 6)
            print(f"Dice rolled: {roll_1} and {roll_2}")
            print("\n".join(dice_faces[roll_1]), sep="\t")
            print("\n".join(dice_faces[roll_2]))
            freq_map_dice_roll[roll_1] += 1
            freq_map_dice_roll[roll_2] += 1
            freq_map_rolls[roll_1 + roll_2] += 1
        elif should_roll_dice.lower() == "No".lower():
            print("Exiting...")
            print(freq_map_dice_roll)
            print(freq_map_rolls)
            done = True
        else:
            print("Please type 'Yes' or 'No'\n")


print("== Dice roller ==")
roll_dice()
