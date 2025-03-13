# b) Sample 1

import random

def getExpression(level, operator):
    if operator == "+":
        operand1 = random.randint(10**(level-1), 10**level - 1)
        operand2 = random.randint(10**(level-1), 10**level - 1)
        result = operand1 + operand2
        expression = f"{operand1} + {operand2} = "
        return expression, result

    elif operator == "-":
        operand1 = random.randint(10**(level-1), 10**level - 1)
        operand2 = random.randint(10**(level-1), operand1 - 1)
        result = operand1 - operand2
        expression = f"{operand1} - {operand2} = "
        return expression, result

    elif operator == "*":
        operand1 = random.randint(10**(level-1), 10**level - 1)
        if level == 1:
            operand1 = random.randint(2, 9)
        operand2 = random.randint(2, 9)
        result = operand1 * operand2
        expression = f"{operand1} * {operand2} = "
        return expression, result

    else:
        raise ValueError("Invalid operator. Use '+', '-', or '*'.")


def main():
    # Get user input for the highest level
    while True:
        try:
            highest_level = int(
                input("Enter highest level to complete (1-5): "))
            if 1 <= highest_level <= 5:
                break
            else:
                print("Highest level must be between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

    current_level = 1  # Start at level 1

    while current_level <= highest_level:
        # Randomly choose an operator
        operator = random.choice(["+", "-", "*"])

        # Generate the expression and result
        expression, result = getExpression(current_level, operator)

        # Ask the user for their answer
        user_answer = input(f"Level {current_level}, {expression}? ")

        # Check if the user's answer is correct
        try:
            user_answer = int(user_answer)
            if user_answer == result:
                print("Correct! Well done!", end=" ")
                if current_level == highest_level:
                    print(
                        f"You have completed the highest level {highest_level}! You have passed.")
                    break
                else:
                    print(f"Proceeding to the next level {current_level + 1}.")
                    current_level += 1
            else:
                print("Incorrect answer.", end=" ")
                if current_level == 1:
                    print("You have failed.")
                    break
                else:
                    print(f"Dropping down to level {current_level - 1}.")
                    current_level -= 1
        except ValueError:
            print("Invalid input. Please enter a number.")


# Run the program
main()
