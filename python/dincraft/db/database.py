from dincraft.domain.table_listener import TableListener

class Database(TableListener):
    def __init__(self, pathToFile: str):
        self._pathToFile = pathToFile

    def update(self):
        pass

    def save(self):
        pass

    def load(self):
        pass