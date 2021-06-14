from sys import argv


def fact(of_number):
    result = 1
    for i in range(0, of_number):
        result += result * i
        yield result


n = int(argv[1])

for el in fact(n):
    print(el)
