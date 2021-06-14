hint = "Enter a line to write to file: "
with open("task1.txt", "a", encoding='utf-8') as file_obj:
    while True:
        line = input(hint)
        if line == '':
            break
        file_obj.write(line)
        file_obj.write("\n")
