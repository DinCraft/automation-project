class Response:
    def __init__(self, code: int, body):
        self._code = code
        self._body = body

    def __str__(self):
        return str(self._body)