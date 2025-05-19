
class Cell:
    _ws = None

    @staticmethod
    def init(ws):
        Cell._ws = ws

    @staticmethod
    def set(day):
        Cell.ws['1'] = 1