from sys import argv


def calc_salary(working_hours, pay_for_hour, bonus):
    return working_hours * pay_for_hour + bonus


try:
    print(f"Salary is: {calc_salary(int(argv[1]), int(argv[2]), int(argv[3]))}")
except ValueError as e:
    print(f"You should enter hours, pay for hour and bonus as three numbers. There was an error: {e}")
