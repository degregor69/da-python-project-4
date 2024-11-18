from tinydb import TinyDB, Query
from .tournaments import Tournament
from ..players.players_manager import PlayersManager


class TournamentsManager:
    def __init__(self, db_path="data/tournaments.json"):
        self.db = TinyDB(db_path).table("tournaments")
        self.db_players = TinyDB(db_path).table("players")
        self.players_manager = PlayersManager()

    def add_tournament(self, tournament: Tournament):
        tournament_as_dict = tournament.to_dict()
        self.db.insert(tournament_as_dict)
        print("Tournoi sauvegardé avec succès")

    def get_all_tournaments(self):
        tournaments_data = self.db.all()
        return [Tournament(**tournaments_data) for tournaments_data in tournaments_data]

    def get_tournament(self, tournament_id: int = None):
        if tournament_id:
            TournamentQuery = Query()
            tournament_data = self.db.get(TournamentQuery.id == tournament_id)
            if not tournament_data:
                return None

    def get_all_players(self):
        return self.players_manager.get_all_players()
