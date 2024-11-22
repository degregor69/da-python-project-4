class Match:
    _id_counter = 1  # Variable de classe pour suivre le prochain ID

    def __init__(
        self,
        player_1: int,
        player_2: int,
        score_player_1: float = 0.0,
        score_player_2: float = 0.0,
    ):
        self.id = Match._id_counter  # Attribuer l'ID unique
        Match._id_counter += 1  # Incrémenter le compteur pour le prochain match
        self.player_1 = player_1
        self.score_player_1 = score_player_1
        self.player_2 = player_2
        self.score_player_2 = score_player_2

    def get_match_as_tuple(self):
        return (
            [self.player_1, self.score_player_1],
            [self.player_2, self.score_player_2],
        )

    def to_dict(self):
        return {
            "id": self.id,  # Inclure l'ID dans le dictionnaire
            "player_1": self.player_1,
            "player_2": self.player_2,
            "score_player_1": self.score_player_1,
            "score_player_2": self.score_player_2,
        }
