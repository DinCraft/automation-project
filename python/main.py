import os
import sqlite3

from dincraft.common.table import Table
from table_command import TableCommand

print("Table maker")

table = Table()

while True:
    command = input()
    args = command.split()
    if args[0] == "open":
        if len(args) != 2:
            print("Error! One argument required: open <pathToFile.db>")
        if not os.path.exists(args[1]):
            print("Error! File doesn't exist!")
            continue
        connection = sqlite3.connect(args[1])
    elif args[0] == "create":
        if len(args) != 2:
            print("Error! One argument required: create <pathToFile.db>")
            continue
        if os.path.exists(args[1]):
            print("Error! File already exists!")
            continue
        connection = sqlite3.connect(args[1])
    else:
        print("Command not found!")