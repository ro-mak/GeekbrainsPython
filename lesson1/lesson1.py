# TASK 1
def task1():
    variable1 = "Some string"
    variable2 = 123
    print(variable1)
    print(variable2)

    variable3 = int(input("Input a number: "))
    variable4 = int(input("Input another number: "))
    variable5 = input("Input a string: ")
    variable6 = input("Input another string: ")
    print(f"You entered numbers 1: {variable3} 2: {variable4} and strings 1: {variable5} 2: {variable6}")


# TASK 2
def task2():
    hour = 60 * 60
    minute = 60
    user_input_seconds = int(input("Input time in seconds: "))
    hours = user_input_seconds // hour
    minutes = (user_input_seconds - (hours * hour)) // minute
    seconds = user_input_seconds - (minutes * minute) - (hours * hour)

    print(format("Time entered: %02d:%02d:%02d" % (hours, minutes, seconds)))


# TASK 3
def task3():
    n_str = input("Enter number n: ")
    n = int(n_str)
    nn = int(n_str + n_str)
    nnn = int(n_str + n_str + n_str)
    print(f"{n} + {nn} + {nnn} = " + str(n + nn + nnn))


# TASK 4
def task4():
    number = input("Input a positive number: ")
    i = 0
    max_n = -1
    while i < len(number):
        cur_n = int(number[i])
        if cur_n > max_n:
            max_n = cur_n
        i += 1
    if max_n != -1:
        print(f"Max number found {max_n}")
    else:
        print("Max number not found")


taskDict = {
    1: task1,
    2: task2,
    3: task3,
    4: task4
}

taskToStart = int(input("Input task number: "))
if taskToStart <= len(taskDict):
    taskDict[taskToStart]()
