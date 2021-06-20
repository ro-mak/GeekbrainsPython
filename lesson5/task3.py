file3 = open("task3.txt")
lines = file3.readlines()
file3.close()
salary_threshold = 20000
total_salary = 0
number_of_people = len(lines)
poor_people_list = []
for line in lines:
    split_line = line.split()
    salary = int(split_line[1])
    total_salary += salary
    if salary < salary_threshold:
        poor_people_list.append(split_line[0])
print(f"Poor people: {poor_people_list}")
print(f"Average salary: {total_salary / number_of_people}")

