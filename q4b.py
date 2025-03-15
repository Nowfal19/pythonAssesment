import random


def getTreasureList():
    # Create a list with 6 ones, 2 zeros, and 2 negative ones
    treasureList = [1] * 6 + [0] * 2 + [-1] * 2
    random.shuffle(treasureList)
    return treasureList


def countTreasures(treasureList, indices):
    # Check if any of the indices point to a bomb (-1)
    if any(treasureList[index] == -1 for index in indices):
        return -1
    # Count the number of treasures (1s) found
    treasure_count = sum(1 for index in indices if treasureList[index] == 1)
    return treasure_count


# Example usage
if __name__ == "__main__":
    # Get the shuffled treasure list
    treasure_list = getTreasureList()
    print("Treasure List:", treasure_list)

    # Simulate player picks (indices)
    player_input = input("Enter your 4 picks (comma-separated, 0-9): ").strip()
    indices = player_input.split(',')  # Split into a list of strings
    picks = [int(index.strip()) for index in indices]  # Convert to integers

    # Count treasures or check for bombs
    result = countTreasures(treasure_list, picks)
    if result == -1:
        print("You hit a bomb!")
    else:
        print(f"You found {result} treasures!")
