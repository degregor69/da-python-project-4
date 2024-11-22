from models.matches.matches_manager import MatchesManager
from models.rounds.rounds import Round
from views.matches import MatchesViews


class SetMatchScoreController:
    def __init__(self, matches_manager: MatchesManager):
        self.matches_manager = matches_manager

    def run(self, round: Round):
        for match in round.matches:
            match_result = MatchesViews.set_match_score(match)
            if match_result == 1:
                match.score_player_1 = 1
                match.score_player_2 = 0
            elif match_result == 2:
                match.score_player_1 = 0
                match.score_player_2 = 1
            else:
                match.score_player_1 = match.score_player_2 = 0.5
            self.matches_manager.update_match(match)

