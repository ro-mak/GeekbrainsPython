time_of_the_year_list = {(1, 2, 12): "winter", (3, 4, 5): "spring", (6, 7, 8): "summer", (9, 10, 11): "autumn"}
while True:
    try:
        month = int(input("Input a month: "))
        if month not in range(1, 13):
            raise Exception("Your number is out of range (1-12)")
        for el in time_of_the_year_list.keys():
            if month in el:
                print(time_of_the_year_list[el])
                break
        break
    except Exception as e:
        print(f"There was an input error({e}). Please, type an int from 1 to 12.")
