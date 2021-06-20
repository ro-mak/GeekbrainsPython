numbers_ru_dict = {1: "Один", 2: "Два", 3: "Три", 4: "Четыре"}
numbers_en_dict = {1: "One", 2: "Two", 3: "Three", 4: "Four"}


def replace_en_with_ru_numbers(en_line):
    temp_line = en_line
    line_split = en_line.split("-")
    number_int = int(line_split[1].strip())
    symbol_index = number_int
    en_symbol = numbers_en_dict[symbol_index]
    ru_symbol = numbers_ru_dict[symbol_index]
    return temp_line.replace(en_symbol, ru_symbol)


en_file = open("task4_en.txt")
ru_file = open("task4_ru.txt", "w", encoding="utf-8")
for line in en_file:
    ru_line = replace_en_with_ru_numbers(line)
    ru_file.write(ru_line)
en_file.close()
ru_file.close()
