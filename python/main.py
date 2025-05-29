import os
import sqlite3

from dincraft.command.table_command import TableCommand

print("Table maker")

while True:
    command = input()
    if len(command) == 0:
        continue
    args = command.split()
    if args[0] == "exit":
        if len(args) != 1:
            print("No arguments required: exit")
            continue
        break

    if args[0] == "open":
        if len(args) != 2:
            print("Error! One argument required: open <pathToFile.db>")
            continue
        if not os.path.exists(args[1]):
            print("Error! File doesn't exist!")
            continue
        connection = sqlite3.connect(args[1])
        continue

    if args[0] == "create":
        if len(args) != 2:
            print("Error! One argument required: create <pathToFile.db>")
            continue
        if os.path.exists(args[1]):
            print("Error! File already exists!")
            continue
        tableCommand = TableCommand(args[1])
        tableCommand.run()
        continue

    print("Command not found!")