def my_func(arg1, arg2, arg3):
    result = sorted((arg1, arg2, arg3))
    return result[1] + result[2]


def my_func_unlimited(*args):
    result = sorted(args)
    return result[len(result) - 2] + result[len(result) - 1]


print(my_func(1, 2, 3))
print(my_func(3, 2, 1))
print(my_func(5, 2, 3))
print(my_func(3, 7, 1))

print(my_func_unlimited(1, 2, 3, 99))
print(my_func_unlimited(3, 2, 1, 143))
print(my_func_unlimited(5, 2, 3, 4, 43, 55))
print(my_func_unlimited(3, 7, 1, 10, 12, 1))
