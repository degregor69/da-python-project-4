from models.tournaments.tournaments_manager import TournamentsManager
from models.tournaments.tournaments import Tournament
from views import tournaments as tournaments_views


class StartTournamentController:
    def __init__(self):
        self.tournaments_manager = TournamentsManager()

    def start_tournament(self):
        # Choose the tournamnent we want to start
        tournament = tournaments_views.get_tournament(self.tournaments_manager)
