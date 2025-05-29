from dincraft.domain.table import Table
from dincraft.domain.table_listener import TableEvent

class Database(TableEvent):
    def __init__(self, parent: Table, pathToFile: str):
        self._parent = parent
        self._pathToFile = pathToFile

    def update(self):
        pass

    def save(self):
        pass

    def load(self):
        pass