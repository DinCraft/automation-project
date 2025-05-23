from dincraft.common.table import Table

print("Table maker")

table = Table()

while True:
    command = input()
    args = command.split()
    if args[0] == "open":
        if len(args) != 2:
            print("Error! One argument required: open <file.db>")
    if args[0] == "create":
    