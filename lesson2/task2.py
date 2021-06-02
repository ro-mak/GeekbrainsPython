def swap(l: list, i: int):
    temp = l[i]
    l[i] = l[i + 1]
    l[i + 1] = temp


try:
    user_list = input("Input a space-separated list: ").split()
    i = 0
    while i in range(len(user_list)):
        if i + 1 < len(user_list):
            swap(user_list, i)
        i += 2

    print(f"List {user_list}")
except Exception as e:
    print(f"Something went wrong: {e}")
