from dincraft.common.employer import Employer
from dincraft.common.response import Response
from dincraft.datetime.months import Months

class Table:
    def __init__(self):
        self._employers = []
        self._month = Months.months[0]
        

    def create(self, id, name, job, workdays, rate):
        self._employers.append(Employer(id, name, job, workdays, rate))

    def read(self, id: int):
        for e in self._employers:
            if e._id == id:
                return Response(0, e)
        return Response(1, "null")

    def update(self, id: int, name: str, job: str, workdays: int, rate: int):
        empl = None
        for e in self._employers:
            if e._id == id:
                empl = e
        if empl == None:
            return Response(1, "null")
        if name != "null":
            empl._name = name
        if job != "null":
            empl._job = job
        if workdays != -1:
            empl._workdays = workdays
        if rate != -1:
            empl._rate = rate
        return Response(0, "null")

    def delete(self, id: int):
        empl = None
        for e in self._employers:
            if e._id == id:
                empl = e
        if empl == None:
            return Response(1, "null")
        self._employers.remove(empl)
        return Response(0, "null")