# Question 2 a
import random


def getExpression(level, operator):
    if operator == "+":
        # Generate two random numbers with 'level' digits
        operand1 = random.randint(10**(level-1), 10**level - 1)
        operand2 = random.randint(10**(level-1), 10**level - 1)
        result = operand1 + operand2
        expression = f"{operand1} + {operand2} = "
        return expression, result

    elif operator == "-":
        # Generate two random numbers with 'level' digits, ensuring operand1 > operand2
        operand1 = random.randint(10**(level-1), 10**level - 1)
        operand2 = random.randint(10**(level-1), operand1 - 1)
        result = operand1 - operand2
        expression = f"{operand1} - {operand2} = "
        return expression, result

    elif operator == "*":
        # Generate the first operand with 'level' digits
        operand1 = random.randint(10**(level-1), 10**level - 1)
        # For level 1, ensure the first operand does not start with 1
        if level == 1:
            operand1 = random.randint(2, 9)
        # The second operand is always a single digit from 2 to 9
        operand2 = random.randint(2, 9)
        result = operand1 * operand2
        expression = f"{operand1} * {operand2} = "
        return expression, result

    else:
        raise ValueError("Invalid operator. Use '+', '-', or '*'.")


expression, result = getExpression(1, "+")
print(expression, result)

expression, result = getExpression(2, "-")
print(expression, result)
