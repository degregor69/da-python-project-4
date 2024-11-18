from models.players.players_manager import PlayersManager
from models.tournaments.tournaments_manager import TournamentsManager
from models.tournaments.tournaments import Tournament
from views import tournaments as tournaments_views


class CreateTournamentController:
    def __init__(self):
        self.tournaments_manager = TournamentsManager()
        self.players_manager = PlayersManager()

    def run(self):
        new_tournament_as_dict = tournaments_views.create_tournament()
        new_tournament = Tournament(**new_tournament_as_dict)

        # Sélection des joueurs
        new_tournament.players_ids = tournaments_views.ask_for_players(
            self.tournaments_manager, self.players_manager
        )

        # Sauvegarder le tournoi dans la base de données
        self.tournaments_manager.add_tournament(new_tournament)
