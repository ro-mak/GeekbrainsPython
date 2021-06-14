file_with_numbers = open("task5.txt", "w")
numbers = [i * 2 for i in range(0, 1001)]
for i, n in enumerate(numbers):
    if i != 0:
        file_with_numbers.write(" ")
    file_with_numbers.write(str(n))

file_with_numbers.close()
file_with_numbers = open("task5.txt")
numbers_from_file = map(int, file_with_numbers.readline().split())

print(f"Sum = {sum(numbers_from_file)}")
file_with_numbers.close()
