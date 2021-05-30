time_of_the_year_list = ["winter", "spring", "summer", "autumn"]
while True:
    try:
        month = int(input("Input a month: "))
        if month not in range(1, 13):
            raise Exception("Your number is out of range (1-12)")
        if month in (1, 2, 12):
            print(time_of_the_year_list[0])
        elif month in (3, 4, 5):
            print(time_of_the_year_list[1])
        elif month in (6, 7, 8):
            print(time_of_the_year_list[2])
        elif month in (9, 10, 11):
            print(time_of_the_year_list[3])
        break
    except Exception as e:
        print(f"There was an input error({e}). Please, type an int from 1 to 12.")
