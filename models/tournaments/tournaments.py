import datetime
from typing import List

from models.players.players import Player
from models.rounds import Round


class Tournament:
    def __init__(
        self,
        name: str,
        location: str,
        start_date: datetime.date,
        end_date: datetime.date,
        description: str = '',
        rounds: List[Round] = [],
        actual_round: int = 0,
        nb_rounds: int = 4,
    ):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.rounds = rounds
        self.actual_round = actual_round
        self.nb_rounds = nb_rounds
        self.description = description

    def get_players(self) -> List[Player]:
        # Rassemble tous les joueurs uniques de chaque match dans tous les rounds
        players_set = {
            player
            for round in self.rounds
            for match in round.matches
            for player in match.get_players()
        }
        return list(players_set)
