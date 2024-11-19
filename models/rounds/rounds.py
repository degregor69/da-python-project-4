import datetime
from typing import List

from models.matches.matches import Match



class Round:
    def __init__(self, name: str, start_datetime: datetime.datetime, end_datetime: datetime.datetime, matches: List[Match]):
        self.name = name
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.matches = matches

