from functools import reduce


def multiply_neighbour_elements(prev_el, el):
    return prev_el * el


result = reduce(multiply_neighbour_elements, [i for i in (range(100, 1001))])

print(result)
