import datetime

from models.rounds import Round


class Tournament:
    def __init__(self, name: str, location: str, start_date: datetime.date, end_date: datetime.date, rounds = [Round], nb_rounds: int = 4,):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.rounds = rounds
        self.nb_rounds = nb_rounds
