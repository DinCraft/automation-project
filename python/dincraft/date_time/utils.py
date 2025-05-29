import datetime

class Utils:
    def get_day_of_week(year, month, day):
        days = ["пн", "вт", "ср", "чт", "пт", "сб", "вс"]
        date = datetime.datetime(year, month, day)
        return days[date.weekday()]
