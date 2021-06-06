numbers_sum = 0
while True:
    input_string = input("Input space-separated numbers: ").split()
    numbers: list[int] = [0]
    shouldStop = False
    for el in input_string:
        try:
            number = int(el)
            numbers.append(number)
        except ValueError:
            shouldStop = True
    for number in numbers:
        numbers_sum += number
    print(f"Result:{numbers_sum}")
    if shouldStop:
        break
