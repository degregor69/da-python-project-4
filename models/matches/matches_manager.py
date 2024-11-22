from tinydb import TinyDB, Query
from models.matches.matches import Match

class MatchesManager:
    def __init__(self, db_path="data/matches.json"):
        self.db = TinyDB(db_path).table("matches")

    def add_match(self, match: Match):
        self.db.insert(match.to_dict())

    def get_match(self, match_id: int) -> Match:
        MatchQuery = Query()
        match_data = self.db.get(MatchQuery.id == match_id)
        if match_data:
            return Match.from_dict(match_data)
        raise ValueError(f"Match avec l'ID {match_id} introuvable.")