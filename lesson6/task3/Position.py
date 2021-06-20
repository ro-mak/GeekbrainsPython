from lesson6.task3.Worker import Worker


class Position(Worker):
    def get_full_name(self):
        return f"Full name: {self.name} {self.surname}"

    def get_total_income(self):
        wage = int(self._income["wage"])
        bonus = int(self._income["bonus"])
        return f"Total income: {wage + bonus}"
