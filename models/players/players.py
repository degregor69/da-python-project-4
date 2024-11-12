import datetime

from tinydb import TinyDB


class Player:
    def __init__(self, last_name: str, first_name: str, birth_date: datetime.date, national_id: str, points: float = 0.0):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.national_id = national_id
        self.points = points

