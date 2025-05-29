from dincraft.domain.employee import Employee
from dincraft.date_time.month import Month
from dincraft.db.database import Database

class Table:
    def __init__(self, pathToFile: str):
        self._employees = []
        self._month = Month(0)
        self._year = 2000
        self._database = Database(pathToFile)

    def create_employee(self) -> Employee:
        e = Employee()
        self._employees.append(e)
        return e

    def save_database(self):
        pass

    def read_database(self):
        pass

    def save_xlsx(self):
        pass

    def notify(self):
        pass
    