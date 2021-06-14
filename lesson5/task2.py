with open("task2.txt", encoding='utf-8') as file_obj:
    line_count = 0
    word_count = 0
    for line in file_obj:
        print(line.replace("\n", ""), end="|||")
        line_count += 1
        line_word_count = len(line.split())
        print(f"Words in line {line_count}: {line_word_count}")
        word_count += line_word_count
    print(f"\nTotal lines in file: {line_count} \nTotal words in file: {word_count}")
