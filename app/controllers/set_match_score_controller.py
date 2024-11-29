from app.models.matches.matches_manager import MatchesManager
from app.models.rounds.rounds import Round
from app.models.rounds.rounds_manager import RoundsManager
from app.views.matches import MatchesViews


class SetMatchScoreController:
    def __init__(self, matches_manager: MatchesManager,
                 rounds_manager: RoundsManager):
        self.matches_manager = matches_manager
        self.rounds_manager = rounds_manager

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
