from typing import List
import datetime

from models.players.players import Player
from models.players.players_manager import PlayersManager
from models.rounds.rounds import Round
from models.rounds.rounds_manager import RoundsManager


class Tournament:
    def __init__(
        self,
        name: str,
        location: str,
        start_date: datetime.date,
        end_date: datetime.date,
        description: str = "",
        players: List[Player] = [],
        rounds: List[Round] = [],
        actual_round: int = 1,
        nb_rounds: int = 4,
    ):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.players = players  # Liste d'objets Player
        self.rounds = rounds
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
            "rounds_ids": [game_round.id for game_round in self.rounds],
            "actual_round": self.actual_round,
            "nb_rounds": self.nb_rounds,
        }

    @classmethod
    def from_dict(cls, data: dict, players_manager: PlayersManager = None, rounds_manager: RoundsManager = None):
        players = [players_manager.get_player(player_id) for player_id in data["players_ids"]]
        rounds = [rounds_manager.get_round(round_id) for round_id in data["rounds_ids"]]
        return cls(
            name=data["name"],
            location=data["location"],
            start_date=datetime.datetime.strptime(data["start_date"], "%Y-%m-%d").date(),
            end_date=datetime.datetime.strptime(data["end_date"], "%Y-%m-%d").date(),
            description=data["description"],
            players=players,
            rounds=rounds,
            actual_round=data["actual_round"],
            nb_rounds=data["nb_rounds"],
        )

    def get_players_points(self):
        players_points = {}
        for round in self.rounds:
            for match in round.matches:
                # Extraire les scores des joueurs
                score_player_1 = match.score_player_1
                score_player_2 = match.score_player_2

                # Ajouter les points pour player_1
                if match.player_1.national_id not in players_points:
                    players_points[match.player_1.national_id] = 0
                players_points[match.player_1.national_id] += score_player_1

                # Ajouter les points pour player_2
                if match.player_2.national_id not in players_points:
                    players_points[match.player_2.national_id] = 0
                players_points[match.player_2.national_id] += score_player_2

        # Convertir le dictionnaire en une liste de tuples et trier par score (valeur) en ordre décroissant
        return sorted(players_points.items(), key=lambda item: item[1], reverse=True)
