from controllers.set_match_score_controller import SetMatchScoreController
from models.matches.matches import Match
from models.matches.matches_manager import MatchesManager
from models.players.players import Player
from models.players.players_manager import PlayersManager
from models.rounds.rounds import Round
from models.rounds.rounds_manager import RoundsManager
from models.tournaments.tournaments import Tournament
from models.tournaments.tournaments_manager import TournamentsManager
from views.tournaments import StartTournamentViews
import random


class StartTournamentController:
    def __init__(self):
        self.tournaments_manager = TournamentsManager()
        self.players_manager = PlayersManager()
        self.matches_manager = MatchesManager()
        self.rounds_manager = RoundsManager()
        self.set_match_score_controller = SetMatchScoreController(self.matches_manager)

    def run(self):
        # Choose the tournamnent we want to start
        tournament = StartTournamentViews.select_tournament(
            self.tournaments_manager)
        StartTournamentViews.display_tournament_actual_round(
            tournament.actual_round)

        # while tournament.actual_round < tournament.nb_rounds - 1:
        
        # Generate rounds
        if tournament.actual_round == 0:
            round = self.generate_first_round(tournament=tournament)
        else:
            round = self.generate_other_rounds(tournament=tournament)
            return
        
        # Update score of the round
        self.set_match_score_controller.run(round)

        # Update the round of the tournament
        tournament.actual_round += 1
        self.tournaments_manager.update_tournament(tournament)


    def generate_first_round(self, tournament: Tournament):
        StartTournamentViews.display_tournament_players(tournament.players)

        # Sorting players
        sorted_players = random.sample(
            tournament.players, len(tournament.players)
        )
        StartTournamentViews.display_sorted_players(sorted_players)

        # Generate matches
        round_matches = self.generate_matches(sorted_players)
        # Create and save round
        round = self.create_and_save_round(
            round_matches, tournament.actual_round)

        StartTournamentViews.display_created_round(round)
        return round

    def generate_classic_round(self, tournament: Tournament):
        # Sort players by points in the tournament


    def generate_matches(self, sorted_players: list[Player]):
        round_matches = []
        while sorted_players:
            new_match = Match(
                player_1=sorted_players.pop(0),
                player_2=sorted_players.pop(0))

            round_matches.append(new_match)
            self.matches_manager.add_match(new_match)
        return round_matches

    def create_and_save_round(
        self,
        round_matches: list[Match],
        actual_round: int,
    ):
        first_round = Round(
            name=f"Round {actual_round}",
            matches=round_matches)
        self.rounds_manager.add_round(first_round)
        return first_round

