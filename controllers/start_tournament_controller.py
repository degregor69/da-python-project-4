from models.players.players import Player

from models.players.players_manager import PlayersManager
from models.tournaments.tournaments_manager import TournamentsManager
from views.tournaments import StartTournamentViews
import random


class StartTournamentController:
    def __init__(self):
        self.tournaments_manager = TournamentsManager()
        self.players_manager = PlayersManager()

    def run(self):
        # Choose the tournamnent we want to start
        tournament = StartTournamentViews.select_tournament(self.tournaments_manager)
        print(f"Joueurs : {tournament.players_ids}")

        # Sorting players
        if (
            tournament.actual_round == 0
        ):  # If beginning of tournament, randomly sort players
            sorted_players = random.sample(
                tournament.players_ids, len(tournament.players_ids)
            )
            print("Joueurs triés aléatoirement :")
            print(sorted_players)
        else:  # if tournament already begun, sort by points
            # TODO points during the tournament, not all points by player
            players: list[Player] = []
            for player_id in tournament.players_ids:
                players.append(self.players_manager.get_player(player_id))
            sorted_players = sorted(
                tournament.players_ids, key=lambda player: player.points
            )

        # Generate pairs
