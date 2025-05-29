from dincraft.domain.table import Table
from dincraft.domain.table_event import TableEvent

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