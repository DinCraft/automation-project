from dincraft.common.table import Table
from dincraft.datetime.month import Month
from employee_command import EmployeeCommand

class TableCommand:
    def __init__(self, pathToFile: str):
        self._pathToFile = pathToFile
        self._file = self._pathToFile[self._pathToFile.rfind("/"):len(self._pathToFile)]
        self._table = Table()

    def run(self):
        while True:
            command = input(self._name)
            args = command.split()

    def set_month(self, month: Month):
        self._table._month = month

    def set_year(self, year):
        self._table._year = year

    def print_interval(self, interval):
        pass

    def create_employee(self):
        employeeCommand = EmployeeCommand()

    def update_employee(self):
        pass