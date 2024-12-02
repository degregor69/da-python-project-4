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
        players =  self.players_manager.get_all_players()
        players_ids = CreateTournamentViews.ask_for_players(players
        )

        players = [self.players_manager.get_player(id) for id in players_ids]
        new_tournament.players = players

        # Sauvegarder le tournoi dans la base de données
        self.tournaments_manager.add_tournament(new_tournament)
