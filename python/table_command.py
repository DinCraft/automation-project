class TableCommand:
    def __init__(self, pathToFile: str):
        self._pathToFile = pathToFile
        self._file = self._pathToFile[self._pathToFile.rfind("/"):len(self._pathToFile)]
        print(self._file)

    def run(self):
        while True:
            command = input(self._name)
            args = command.split()
