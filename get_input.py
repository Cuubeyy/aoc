import os
from datetime import date
from aocd import get_data


class GetInput:
    def __init__(self):
        self.session = os.environ.get("AOC_SESSION")

    def get_today(self):
        year, month, day = str(date.today()).split("-")

        return get_data(self.session, int(day), int(year), True)
