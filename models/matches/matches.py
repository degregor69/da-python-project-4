from models.players.players import Player
from models.players.players_manager import PlayersManager


class Match:
    _id_counter = 1  # Variable de classe pour suivre le prochain ID

    def __init__(
        self,
        player_1: Player,
        player_2: Player,
        score_player_1: float = 0.0,
        score_player_2: float = 0.0,
    ):
        self.id = Match._id_counter  # Attribuer l'ID unique
        Match._id_counter += 1  # Incrémenter le compteur pour le prochain match
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_player_1 = score_player_1
        self.score_player_2 = score_player_2

    def to_dict(self):
        return {
            "id": self.id,
            "player_1": self.player_1.national_id,
            "player_2": self.player_2.national_id,
            "score_player_1": self.score_player_1,
            "score_player_2": self.score_player_2,
        }

    @classmethod
    def from_dict(cls, data: dict, players_manager: PlayersManager):
        player_1 = players_manager.get_player(data["player_1"])
        player_2 = players_manager.get_player(data["player_2"])
        return cls(
            player_1=player_1,
            player_2=player_2,
            score_player_1=data["score_player_1"],
            score_player_2=data["score_player_2"]
        )

    def get_match_as_tuple(self):
        return (
            [self.player_1.national_id, self.score_player_1],
            [self.player_2.national_id, self.score_player_2],
        )
