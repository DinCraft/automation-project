from dincraft.domain.employee import Employee
from dincraft.date_time.month import Month

class Table:
    def __init__(self):
        self._employers = []
        self._month = Month(0)
        self._year = 2000

    def save_database(self):
        pass

    def read_database(self):
        pass

    def save_xlsx(self):
        pass

    def notify(self):
        pass
    