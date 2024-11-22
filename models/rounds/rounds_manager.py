from tinydb import TinyDB, Query

from models.rounds.rounds import Round


class RoundsManager:
    def __init__(self, db_path="data/rounds.json"):
        self.db = TinyDB(db_path).table("rounds")

    def add_round(self, round: Round):
        self.db.insert(round.to_dict())
