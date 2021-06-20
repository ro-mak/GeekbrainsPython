lessons_file = open("task6.txt", encoding="utf-8")
lessons_dict = dict()
for line in lessons_file:
    lesson_info = line.split()
    lesson_name = lesson_info[0][:-1]
    lesson_hours = 0
    for info in lesson_info[1:]:
        if info[0].isnumeric():
            hours = int(info.split("(")[0])
            lesson_hours += hours
    lessons_dict[lesson_name] = lesson_hours
lessons_file.close()
print(f"Dict: {lessons_dict}")
