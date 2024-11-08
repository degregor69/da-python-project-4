from models.players import Player


class Match:
    def __init__(self, player_1: Player, score_player_1: float,player_2: Player, score_player_2: float):
        self.player_1 = player_1
        self.score_player_1 = score_player_1
        self.player_2 = player_2
        self.score_player_2 = score_player_2

    def get_match_as_tuple(self):
        return ([self.player_1, self.score_player_1], [self.player_2, self.score_player_2])