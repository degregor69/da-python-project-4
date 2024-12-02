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
        self.set_match_score_controller = SetMatchScoreController(
            self.matches_manager, self.rounds_manager)

    def run(self):
        # Choose the tournamnent we want to start
        all_tournaments = self.tournaments_manager.get_all_tournaments()
        tournament = StartTournamentViews.select_tournament(all_tournaments)
        StartTournamentViews.display_tournament_actual_round(
            tournament.actual_round)

        if tournament.actual_round <= tournament.nb_rounds and tournament.actual_round > 0:
            # Check if a round for the actual round already exists
            if len(tournament.rounds) >= tournament.actual_round:
                round = tournament.rounds[tournament.actual_round - 1]
            else:
                # Generate a new one if it does not exist
                round = (
                    self.generate_first_round(tournament)
                    if tournament.actual_round == 1
                    else self.generate_generic_round(tournament)
                )
                tournament.rounds.append(round)

            # Update score of the round
            self.set_match_score_controller.run(round)

            # Update the round of the tournament
            if tournament.actual_round == tournament.nb_rounds:
                tournament.actual_round = -1
            else:
                tournament.actual_round += 1
            self.tournaments_manager.update_tournament(tournament)

        else:
            StartTournamentViews.display_finished_tournament(tournament)

    def generate_generic_round(self, tournament: Tournament):
        players_ids_by_points_desc = tournament.get_players_points()
        sorted_players = []
        for player_data in players_ids_by_points_desc:
            player = self.players_manager.get_player(player_data[0])
            sorted_players.append(player)

        # Generate matches
        round_matches = self.generate_matches(sorted_players, tournament)
        # Create and save round
        round = self.create_and_save_round_with_tournament_update(
            round_matches, tournament.actual_round)

        StartTournamentViews.display_created_round(round)
        return round

    def generate_first_round(self, tournament: Tournament):
        StartTournamentViews.display_tournament_players(tournament.players)

        # Sorting players
        sorted_players = random.sample(
            tournament.players, len(tournament.players)
        )
        StartTournamentViews.display_sorted_players(sorted_players)

        # Generate matches
        round_matches = self.generate_matches_in_first_round(sorted_players)
        # Create and save round
        round = self.create_and_save_round_with_tournament_update(
            round_matches, tournament.actual_round)

        # Add the round to the tournament and update it
        tournament.rounds.append(round)
        self.tournaments_manager.update_tournament(tournament)

        StartTournamentViews.display_created_round(round)
        return round

    def generate_matches_in_first_round(self, sorted_players: list[Player]):
        round_matches = []
        while sorted_players:
            new_match = Match(
                player_1=sorted_players.pop(0),
                player_2=sorted_players.pop(0))

            round_matches.append(new_match)
            self.matches_manager.add_match(new_match)
        return round_matches

    def generate_matches(
            self, sorted_players: list[Player], tournament: Tournament = None):
        already_played_matches = self.get_already_played_matches(tournament)
        round_matches = []

        skipped_players = []  # To keep players without new opponents
        while sorted_players:
            player_1 = sorted_players.pop(0)
            player_2 = None

            # Search for an opponent for first player
            for i, potential_opponent in enumerate(sorted_players):
                if (player_1.national_id, potential_opponent.national_id) not in already_played_matches and \
                        (potential_opponent.national_id, player_1.national_id) not in already_played_matches:
                    player_2 = sorted_players.pop(i)
                    break

            if player_2:  # Found new pair
                new_match = Match(player_1=player_1, player_2=player_2)
                round_matches.append(new_match)
                self.matches_manager.add_match(new_match)
            else:  # No new player found
                skipped_players.append(player_1)

            # If only skipped players remaining
            if not sorted_players and skipped_players:
                sorted_players.extend(skipped_players)
                skipped_players.clear()
                break

        # Creates matches even if the matches have been already played
        while len(sorted_players) > 1:
            player_1 = sorted_players.pop(0)
            player_2 = sorted_players.pop(0)

            new_match = Match(player_1=player_1, player_2=player_2)
            round_matches.append(new_match)
            self.matches_manager.add_match(new_match)

        return round_matches

    @staticmethod
    def get_already_played_matches(tournament: Tournament):
        return [
            (match.player_1.national_id, match.player_2.national_id)
            for round in tournament.rounds
            for match in round.matches
        ]

    def create_and_save_round_with_tournament_update(
        self,
        round_matches: list[Match],
        actual_round: int,
    ):
        first_round = Round(
            name=f"Round {actual_round}",
            matches=round_matches)
        self.rounds_manager.add_round(first_round)
        return first_round
