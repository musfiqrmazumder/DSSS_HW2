import unittest
from math_quiz import generate_random_integer_number, select_random_operator, generate_quiz_and_answer
class TestMathGame(unittest.TestCase):

    def test_generate_random_integer_number(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_select_random_operator(self):
        # Test if the function returns only one of the allowed operators
        allowed_operators = {'+', '-', '*'}
        for _ in range(1000): #Test a large number of random options
            operator = select_random_operator()
            self.assertTrue(operator, allowed_operators)
        pass

    def test_generate_quiz_and_answer(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (7, 3, '-', '7 - 3', 4), #added 2 more test cases
                (4, 7, '*', '4 * 7', 28),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = generate_quiz_and_answer(num1, num2, operator) #call the function
                self.assertEqual(problem, expected_problem) #assert that the generated problem matches the expected problem
                self.assertEqual(answer, expected_answer)  #assert that the generated problem answer the expected answer
                pass
        
if __name__ == "__main__":
    unittest.main()
