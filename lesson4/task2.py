some_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_list = [x for ind, x in enumerate(some_list) if ind - 1 > 0 if some_list[ind - 1] < some_list[ind]]
print(result_list)
