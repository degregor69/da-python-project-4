from models.tournaments.tournaments_manager import TournamentsManager
from models.tournaments.tournaments import Tournament
from views.tournaments import StartTournamentViews


class StartTournamentController:
    def __init__(self):
        self.tournaments_manager = TournamentsManager()

    def run(self):
        # Choose the tournamnent we want to start
        tournament = StartTournamentViews.select_tournament(self.tournaments_manager)
