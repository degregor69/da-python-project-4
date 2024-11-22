from models.tournaments import tournaments_manager


class UpdateTournamentController:
    def __init__(self, tournament: Tournament, tournaments_manager: TournamentsManager):
        self.tournament = tournament
        self.tournaments_manager = tournaments_manager

    def run(self):
        self.tournaments_manager.update_tournament()
