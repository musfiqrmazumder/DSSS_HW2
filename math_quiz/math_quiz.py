import random

def generate_random_integer_number(min_val, max_val):
    """
    Generate a random integer between min_val and max_val.

    Arguments:
        min_val (int): The minimum value for the random integer.
        max_val (int): The maximum value for the random integer.

    Returns:
        int: A randomly generated integer within the specified range.
    """
    return random.randint(min_val, max_val)


def select_random_operator():
    """
    Select a random mathematical operator from '+', '-', or '*'.

    Returns:
        str: A random operator as a string.
    """
    return random.choice(['+', '-', '*'])


def generate_quiz_and_answer(num1, num2, operator):
    """
    Generate a math problem and calculate its answer based on the operator.

    Arguments:
        num1 (int): The first number in the problem.
        num2 (int): The second number in the problem.
        operator (str): The operator to use ('+', '-', '*').

    Returns:
        tuple: A tuple containing the problem as a string and the answer as an integer.
    """
    problem = f"{num1} {operator} {num2}"

    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    else:
        raise ValueError("Invalid operator. Expected '+', '-', or '*'.")

    return problem, answer


def math_quiz():
    """
    Conduct a simple math quiz with randomly generated math problems.

    The user will be presented with a series of math problems and must provide the correct answers.
    At the end, the user's score is displayed.
    """
    score = 0
    total_questions = 5  # Number of questions in the quiz

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer_number(1, 10)

        # Error handling for the range of numbers
        try:
            num2 = generate_random_integer_number(1, 5)  # Upper limit should be an integer
        except ValueError as e:
            print(f"Error in generating a random number: {e}")
            return

        operator = select_random_operator()
        problem, answer = generate_quiz_and_answer(num1, num2, operator)

        print(f"\nQuestion: {problem}")
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
