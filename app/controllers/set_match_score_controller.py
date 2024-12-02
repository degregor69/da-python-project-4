from datetime import datetime

from models.matches.matches_manager import MatchesManager
from models.rounds.rounds import Round
from models.rounds.rounds_manager import RoundsManager
from views.matches import MatchesViews


class SetMatchScoreController:
    def __init__(self, matches_manager: MatchesManager,
                 rounds_manager: RoundsManager):
        self.matches_manager = matches_manager
        self.rounds_manager = rounds_manager

    def run(self, round: Round):
        for match in round.matches:
            # Check if the scores have already been set up
            if match.score_player_1 + match.score_player_2 > 0.0:
                MatchesViews.already_finished_match(match)
                continue

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
        # Update end time of round when all matches are done
        round.end_datetime = datetime.now()
        self.rounds_manager.update_round(round)