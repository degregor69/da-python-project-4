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

    def _get_next_id(self):
        if len(self.db) > 0:
            last_round = self.db.all()[-1]  # Get last registered
            return last_round["id"] + 1  # Add 1 to its id
        return 1 # if db empty return 1 because first one to be saved
    
    def add_tournament(self, tournament: Tournament):
        tournament.id = self._get_next_id()
        tournament_as_dict = tournament.to_dict()
        self.db.insert(tournament_as_dict)


    def get_all_tournaments(self):
        tournaments_data = self.db.all()
        return [Tournament.from_dict(tournaments_data, self.players_manager, self.rounds_manager)for tournaments_data in tournaments_data]

    def update_tournament(self, tournament: Tournament):
        TournamentQuery = Query()
        self.db.update(tournament.to_dict(), TournamentQuery.id == tournament.id)