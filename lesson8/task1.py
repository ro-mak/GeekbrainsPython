class DateValidationError(Exception):
    pass


class Date:
    def __init__(self, date):
        self.date = date
        int_date = self.parse_date_to_int(date)
        self.validate_date(int_date[0], int_date[1], int_date[2])

    @classmethod
    def parse_date_to_int(cls, date):
        splitted_date = date.split("-")
        return int(splitted_date[0]), int(splitted_date[1]), int(splitted_date[2])

    @staticmethod
    def validate_date(day, month, year):
        if day not in range(1, 32):
            raise DateValidationError(f"Day {day} is not in range 1 - 31")
        if month not in range(1, 13):
            raise DateValidationError(f"Month {month} is not in range 1 - 12")
        if year not in range(0, 2021):
            raise DateValidationError(f"Year {year} is not in range 0 - 2021")


date_list = [
    "20-01-1992",
    "20-01-2992",
    "20-13-1992",
    "32-01-1992",
    "00-01-1992"
]
for date in date_list:
    try:
        Date(date)
    except DateValidationError as err:
        print(err)
