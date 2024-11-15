from tinydb import TinyDB, Query
from .tournaments import Tournament


class TournamentsManager:
    def __init__(self, db_path="data/players.json"):
        self.db = TinyDB(db_path).table("tournaments")
        self.db_players = TinyDB(db_path).table("players")

    def add_tournament(self, tournament: Tournament):
        self.db.insert(tournament.__dict__)

    def get_tournament(self, tournament_id: int):
        TournamentQuery = Query()
        tournament_data = self.db.get(TournamentQuery.id == tournament_id)
        if not tournament_data:
            return "Tournament not found."
        return Tournament(**tournament_data)

    def get_players(self):
        # Récupérer la liste des joueurs dans la base de données
        db_players = self.db_players.all()
        for db_player in db_players:
            print(
                f"{db_player['national_id']} {db_player['first_name']} {db_player['last_name']}"
            )
