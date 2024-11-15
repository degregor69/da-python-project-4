from tinydb import TinyDB, Query
from .tournaments import Tournament
from ..players.players_manager import PlayersManager


class TournamentsManager:
    def __init__(self, db_path="data/tournaments.json"):
        self.db = TinyDB(db_path).table("tournaments")
        self.db_players = TinyDB(db_path).table("players")
        self.players_manager = PlayersManager()

    def add_tournament(self, tournament: Tournament):
        players_as_list_of_dict = [player.__dict__ for player in tournament.players]
        tournament_as_dict = tournament.__dict__
        tournament_as_dict["start_date"] = str(tournament_as_dict["start_date"])
        tournament_as_dict["end_date"] = str(tournament_as_dict["end_date"])
        tournament_as_dict["players"] = players_as_list_of_dict
        self.db.insert(tournament_as_dict)
        print("Tournoi sauvegardé avec succès")

    def get_tournament(self, tournament_id: int):
        TournamentQuery = Query()
        tournament_data = self.db.get(TournamentQuery.id == tournament_id)
        if not tournament_data:
            return "Tournament not found."
        return Tournament(**tournament_data)

    def get_all_players(self):
        return self.players_manager.get_all_players()
