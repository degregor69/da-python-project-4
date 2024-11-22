from tinydb import TinyDB, Query
from .tournaments import Tournament
from ..players.players_manager import PlayersManager
from ..rounds.rounds_manager import RoundsManager


class TournamentsManager:
    def __init__(self, db_path="data/tournaments.json"):
        self.db = TinyDB(db_path).table("tournaments")
        self.db_players = TinyDB(db_path).table("players")
        self.players_manager = PlayersManager()
        self.rounds_manager = RoundsManager()

    def add_tournament(self, tournament: Tournament):
        tournament_as_dict = tournament.to_dict()
        self.db.insert(tournament_as_dict)
        print("Tournoi sauvegardé avec succès")

    def get_all_tournaments(self):
        tournaments_data = self.db.all()
        return [Tournament.from_dict(tournaments_data, self.players_manager, self.rounds_manager)for tournaments_data in tournaments_data]


    def update_tournament(self, tournament: Tournament):
        self.db.update(tournament.to_dict())
        print("Tournoi mis à jour avec succès.")