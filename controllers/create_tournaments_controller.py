from models.players.players_manager import PlayersManager
from models.tournaments.tournaments_manager import TournamentsManager
from models.tournaments.tournaments import Tournament
from views.tournaments import CreateTournamentViews


class CreateTournamentController:
    def __init__(self):
        self.tournaments_manager = TournamentsManager()
        self.players_manager = PlayersManager()

    def run(self):
        new_tournament_as_dict = CreateTournamentViews.create_tournament()
        new_tournament = Tournament(**new_tournament_as_dict)

        # Sélection des joueurs
        new_tournament.players_ids = CreateTournamentViews.ask_for_players(
            self.tournaments_manager, self.players_manager
        )

        # Sauvegarder le tournoi dans la base de données
        self.tournaments_manager.add_tournament(new_tournament)
