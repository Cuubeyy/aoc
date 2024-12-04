import os
from datetime import date
import requests


class Input:
    def __init__(self, day=None, year=None):
        self.task = None

        if day is None:
            self.day = int(str(date.today()).split("-")[2])
        elif isinstance(day, str) or isinstance(day, int):
            self.day = int(day)
        else:
            raise ValueError("Day must be a string or integer.")
        if year is None:
            self.year = int(str(date.today()).split("-")[0])
        elif isinstance(year, str) and isinstance(year, int):
            self.year = int(year)
        else:
            raise ValueError("Year must be a string or integer.")

        self.save_path = f"./inputs/{self.year}/{str(self.day).zfill(2)}.in"

    def get_input(self):
        if os.path.exists(self.save_path):
            return self.open_input()
        url = f"https://adventofcode.com/{self.year}/day/{self.day}/input"
        cookie = os.getenv("AOC_SESSION")
        response = requests.get(url, cookies={"session": cookie})
        self.task = response.content.decode("utf-8")
        self.save_file()
        return self.task

    def save_file(self):
        if not self.task:
            raise Exception("No task found")
        os.makedirs(os.path.dirname(self.save_path), exist_ok=True)
        with open(self.save_path, "w+") as file:
            file.write(self.task)
            file.close()

    def open_input(self):
        if not os.path.exists(self.save_path):
            raise Exception("No task found")
        return open(self.save_path).read()

