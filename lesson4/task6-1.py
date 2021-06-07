from itertools import count
from sys import argv

start_number = int(argv[1])
for i in count(start_number):
    print(i)
    if i >= start_number + 10:
        break
