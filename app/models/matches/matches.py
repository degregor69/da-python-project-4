from models.players.players import Player
from models.players.players_manager import PlayersManager


class Match:
    def __init__(
        self,
        player_1: Player,
        player_2: Player,
        id: int = None,  # ID optionnel
        score_player_1: float = 0.0,
        score_player_2: float = 0.0,
    ):
        self.id = id  # ID est passé en paramètre, mais pas encore défini si None
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
            id=data["id"],  # L'ID est récupéré depuis les données de la base
            player_1=player_1,
            player_2=player_2,
            score_player_1=data["score_player_1"],
            score_player_2=data["score_player_2"],
        )

    def get_match_as_tuple(self):
        return (
            [self.player_1.national_id, self.score_player_1],
            [self.player_2.national_id, self.score_player_2],
        )
