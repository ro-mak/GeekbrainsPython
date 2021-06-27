class CustomZeroDivisionException(Exception):
    pass


while True:
    in1, in2 = [int(input(f"Input a {i} number: ")) for i in range(0, 2)]
    try:
        if in2 == 0:
            raise CustomZeroDivisionException()
        print(in1 / in2)
        break
    except CustomZeroDivisionException:
        print("You cannot divide by zero")
        pass
