from tinydb import TinyDB, Query
from models.matches.matches import Match
from models.players.players_manager import PlayersManager


class MatchesManager:
    def __init__(self, db_path="data/matches.json"):
        self.db = TinyDB(db_path).table("matches")
        self.players_manager = PlayersManager()

    def add_match(self, match: Match):
        self.db.insert(match.to_dict())

    def get_match(self, match_id: int) -> Match:
        MatchQuery = Query()
        match_data = self.db.get(MatchQuery.id == match_id)
        if match_data:
            return Match.from_dict(match_data, self.players_manager)
        raise ValueError(f"Match avec l'ID {match_id} introuvable.")

    def update_match(self, match: Match):
        MatchQuery = Query()
        match_data = match.to_dict()
        updated = self.db.update(match_data, MatchQuery.id == match.id)

        if updated:
            print(f"Le match avec l'ID {match.id} a été mis à jour.")
        else:
            raise ValueError(
                f"Match avec l'ID {match.id} introuvable ou aucune modification effectuée.")
