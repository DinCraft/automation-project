import os
from dincraft.domain.table import Table
from dincraft.date_time.month import Month
from dincraft.command.employee_command import EmployeeCommand

class TableCommand:
    def __init__(self, pathToFile: str):
        self._pathToFile = pathToFile
        self._name = os.path.basename(pathToFile)
        self._table = Table()

    def run(self):
        while True:
            command = input("tm>" + self._name + "> ")
            if len(command) == 0:
                continue
            args = command.split()
            if args[0] == "exit":
                if len(args) != 1:
                    print("No arguments required: exit")
                    continue
                break

            if args[0] == "create":
                if len(args) != 1:
                    print("No arguments required: exit")
                    continue
                


    def set_month(self, month: Month):
        self._table._month = month
        self._table.notify()

    def set_year(self, year):
        self._table._year = year

    def print_interval(self, interval):
        pass

    def create_employee(self):
        employeeCommand = EmployeeCommand()

    def update_employee(self):
        pass