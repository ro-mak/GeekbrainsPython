CRED = '\033[91m'
CEND = '\033[0m'


def divide(number_one: int, number_two: int):
    return number_one / number_two


number_1 = input("Input first number: ")
number_2 = input("Input second number: ")

try:
    print(f"Result = {divide(int(number_1), int(number_2))}")
except ValueError as e:
    print(f"{CRED}There was an error: {e}{CEND}")
except ZeroDivisionError:
    print(f"{CRED}Division by zero is not allowed{CEND}")
