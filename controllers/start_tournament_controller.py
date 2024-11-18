from models.tournaments.tournaments_manager import TournamentsManager
from models.tournaments.tournaments import Tournament
from views.tournaments import StartTournamentViews


class StartTournamentController:
    def __init__(self):
        self.tournaments_manager = TournamentsManager()

    def run(self):
        # Choose the tournamnent we want to start
        tournament = StartTournamentViews.select_tournament(self.tournaments_manager)
        print(tournament.to_dict())

        # TODO
        # IF ACTUAL_ROUND == 0:
        # RANDOMLY SORT THE PLAYER

        # IF ACTUAL ROUND > 0
        # SORT THE PLAYERS BY POINTS
        # ATTRIBUTE FIRST PLAYER TO NEXT ONE EXCEPT IF ALREADY PLAYED AGAINST
        # RUN THIS UNTIL ALL PLAYERS ATTRIBUTED
