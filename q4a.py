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


# # Call getTreasureList() to generate the treasure list
# treasureList = getTreasureList()
# print("Treasure List:", treasureList)

# # Define the indices (player picks)
# indices = [9, 7, 6, 5]  # Use a list of integers

# # Call countTreasures() and print the result
# result = countTreasures(treasureList, indices)
# if result == -1:
#     print("You hit a bomb!")
# else:
#     print(f"You found {result} treasures!")
