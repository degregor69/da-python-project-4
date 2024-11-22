from typing import List
import datetime

from models.players.players import Player
from models.players.players_manager import PlayersManager


class Tournament:
    def __init__(
        self,
        name: str,
        location: str,
        start_date: datetime.date,
        end_date: datetime.date,
        description: str = "",
        players: List[Player] = [],  # Liste des objets Player
        rounds_ids: List[int] = [],
        actual_round: int = 0,
        nb_rounds: int = 4,
    ):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.players = players  # Liste d'objets Player
        self.rounds_ids = rounds_ids
        self.actual_round = actual_round
        self.nb_rounds = nb_rounds

    def to_dict(self):
        return {
            "name": self.name,
            "location": self.location,
            "start_date": str(self.start_date),
            "end_date": str(self.end_date),
            "description": self.description,
            "players_ids": [player.national_id for player in self.players],
            "rounds_ids": self.rounds_ids,
            "actual_round": self.actual_round,
            "nb_rounds": self.nb_rounds,
        }

    @classmethod
    def from_dict(cls, data: dict, players_manager: PlayersManager):
        players = [players_manager.get_player(player_id) for player_id in data["players_ids"]]
        return cls(
            name=data["name"],
            location=data["location"],
            start_date=datetime.datetime.strptime(data["start_date"], "%Y-%m-%d").date(),
            end_date=datetime.datetime.strptime(data["end_date"], "%Y-%m-%d").date(),
            description=data["description"],
            players=players,
            rounds_ids=data["rounds_ids"],
            actual_round=data["actual_round"],
            nb_rounds=data["nb_rounds"],
        )
