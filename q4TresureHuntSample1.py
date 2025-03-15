import random


def create_slots():
    # Create a list with 6 ones, 2 zeros, and 2 negative ones
    slots = [1] * 6 + [0] * 2 + [-1] * 2
    # Shuffle the list to randomize the positions
    random.shuffle(slots)
    return slots


def get_player_picks():
    while True:
        try:
            # Get the player's picks and split them into a list of strings
            picks = input(
                "Enter your 4 picks (comma-separated, 0-9): ").strip().split(',')
            # Convert the picks to integers
            picks = [int(pick.strip()) for pick in picks]
            # Validate that the player entered exactly 4 unique picks within the range 0-9
            if len(picks) != 4:
                print("Please enter exactly 4 picks.")
                continue
            if any(pick < 0 or pick > 9 for pick in picks):
                print("Picks must be between 0 and 9.")
                continue
            if len(picks) != len(set(picks)):
                print("Picks must be unique.")
                continue
            return picks
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas.")


def check_picks(slots, picks):
    # Check the picks and count the number of treasures and bombs
    treasures = 0
    bombs = 0
    for pick in picks:
        if slots[pick] == 1:
            treasures += 1
        elif slots[pick] == -1:
            bombs += 1
    return treasures, bombs


def treasure_hunt_game():
    slots = create_slots()
    chances = 5
    treasures_found = 0

    print("The treasures are planted... You have 5 chances!!")

    for round_num in range(1, chances + 1):
        print(f"Round {round_num}: ", end="")
        picks = get_player_picks()
        treasures, bombs = check_picks(slots, picks)

        if bombs > 0:
            print("You hit a bomb!!")
        else:
            treasures_found += treasures
            print(f"You got {treasures} hits!!")

        if treasures_found >= 4:
            print("You are the winner!!")
            break

    if treasures_found < 4:
        print("You lost!!")

    # print("The hidden list was:")
    # print(slots)


if __name__ == "__main__":
    treasure_hunt_game()
