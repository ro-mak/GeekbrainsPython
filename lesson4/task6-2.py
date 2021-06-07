from itertools import cycle
from sys import argv

repeat_list_elements = argv[1:]
counter = 0
for i in cycle(repeat_list_elements):
    print(i)
    if counter >= 10:
        break
    counter += 1
