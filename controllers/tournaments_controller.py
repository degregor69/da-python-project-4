from models.tournaments.tournaments_manager import TournamentsManager
from models.tournaments.tournaments import Tournament
from views import tournaments as tournaments_views


class TournamentController:
    def __init__(self):
        self.tournaments_manager = TournamentsManager()

    def create_tournament(self):
        new_tournament_as_dict = tournaments_views.create_tournament()
        new_tournament = Tournament(**new_tournament_as_dict)

        # Sélection des joueurs
        new_tournament.players = tournaments_views.ask_for_players(
            self.tournaments_manager
        )

        # Sauvegarder le tournoi dans la base de données
        self.tournaments_manager.add_tournament(new_tournament)
