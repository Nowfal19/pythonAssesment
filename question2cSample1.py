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
    # Get user input for the number of correct answers required
    while True:
        try:
            correct_required = int(input(
                "Enter number of correct answers before proceeding to the next level (2-5): "))
            if 2 <= correct_required <= 5:
                break
            else:
                print("Number of correct answers must be between 2 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 2 and 5.")

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
    correct_count = 0  # Track correct answers at the current level
    incorrect_count = 0  # Track incorrect answers at the current level

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
                correct_count += 1
                incorrect_count = 0  # Reset incorrect count
                print("Correct!", end=" ")
                if correct_count == correct_required:
                    print(
                        f"Well done! You have answered {correct_required} questions correctly, proceeding to the next level {current_level + 1}.")
                    current_level += 1
                    correct_count = 0  # Reset correct count for the next level
                else:
                    print(
                        f"Answer the next {correct_required - correct_count} questions correctly to proceed to the next level.")
            else:
                incorrect_count += 1
                correct_count = 0  # Reset correct count
                print(f"Wrong! The answer is {result}.", end=" ")
                if incorrect_count == correct_required:
                    if current_level == 1:
                        print(
                            "Sorry, you have answered wrongly at level 1! You have failed.")
                        break
                    else:
                        print(
                            f"Sorry, you have answered {correct_required} questions wrongly, dropping to level {current_level - 1}.")
                        current_level -= 1
                        incorrect_count = 0  # Reset incorrect count for the next level
                else:
                    print(
                        f"If you answer the next {correct_required - incorrect_count} questions wrongly, you will drop one level.")
        except ValueError:
            print("Invalid input. Please enter a number.")


# Run the program
main()
