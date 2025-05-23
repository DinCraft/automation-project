class Employer:
    def __init__(self, id: int, name: str, job: str, workdays: int, rate: int):
        self._id = id
        self._name = name
        self._job = job
        self._workdays = workdays
        self._rate = rate

    def __str__(self):
        return "{" \
            + "\"" + "id" + "\":" + str(self._id) + "," \
            + "\"" + "name" + "\":\"" + str(self._name) + "\"," \
            + "\"" + "job" + "\":\"" + str(self._job) + "\"," \
            + "\"" + "workdays" + "\":" + str(self._workdays) + "," \
            + "\"" + "rate" + "\":" + str(self._rate) + "" \
            + "}"
