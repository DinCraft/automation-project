from dincraft.domain.table_listener import TableEvent
from dincraft.domain.table import Table

class XlsxGenerator(TableEvent):
    def __init__(self, table: Table):
        self._table = table

    def save(self):
        pass