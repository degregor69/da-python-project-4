from tinydb import TinyDB, Query

from models.matches.matches_manager import MatchesManager
from models.rounds.rounds import Round


class RoundsManager:
    def __init__(self, db_path="data/rounds.json"):
        self.db = TinyDB(db_path).table("rounds")
        self.matches_manager = MatchesManager()

    def add_round(self, round: Round):
        self.db.insert(round.to_dict())

    def get_round(self, round_id: int):
        RoundQuery = Query()
        round_data = self.db.get(RoundQuery.id == round_id)
        if round_data:
            return Round.from_dict(round_data, self.matches_manager)
        raise ValueError(f"Round avec l'ID {round_id} introuvable.")