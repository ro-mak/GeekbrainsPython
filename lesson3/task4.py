def my_func_first(x, y: int):
    if x < 0:
        raise ValueError("x should be bigger than zero")
    if y > 0:
        raise ValueError("y should be lesser than zero")
    return x ** y


def my_func_second(x, y: int):
    if x < 0:
        raise ValueError("x should be bigger than zero")
    if y > 0:
        raise ValueError("y should be lesser than zero")
    result = 1
    for i in range(0, abs(y)):
        result *= 1/x
    return result


print(my_func_first(16, -3))
print(my_func_second(16, -3))
