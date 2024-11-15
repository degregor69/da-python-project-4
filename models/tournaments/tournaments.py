import datetime
from typing import List


class Tournament:
    def __init__(
        self,
        name: str,
        location: str,
        start_date: datetime.date,
        end_date: datetime.date,
        description: str = "",
        players_ids: List[int] = [],
        rounds_ids: List[int] = [],
        actual_round: int = 0,
        nb_rounds: int = 4,
    ):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.players_ids = players_ids
        self.rounds_ids = rounds_ids
        self.actual_round = actual_round
        self.nb_rounds = nb_rounds
