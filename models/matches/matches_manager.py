from tinydb import TinyDB, Query

from models.matches.matches import Match
from models.players.players_manager import PlayersManager


class MatchesManager:
    def __init__(self, db_path="data/matches.json"):
        self.db = TinyDB(db_path).table("matches")
        self._id_counter = self._get_next_id()  # On charge l'ID suivant pour les nouveaux matchs
        self.players_manager = PlayersManager()

    def _get_next_id(self):

        if len(self.db) > 0:
            last_match = self.db.all()[-1]  # Récupère le dernier match enregistré
            return last_match["id"] + 1  # Incrémente de 1 l'ID du dernier match
        return 1

    def add_match(self, match: Match):
        if match.id is None:
            match.id = self._id_counter  # Attribue l'ID unique du compteur
            self._id_counter += 1  # Incrémente le compteur pour le prochain match
        self.db.insert(match.to_dict())

    def get_match(self, match_id):
        match_data = self.db.get(Query().id == match_id)
        if match_data:
            return Match.from_dict(match_data, self.players_manager)
        return None

    def update_match(self, match: Match):
        MatchQuery = Query()
        match_data = match.to_dict()
        updated = self.db.update(match_data, MatchQuery.id == match.id)

        if updated:
            print(f"Le match avec l'ID {match.id} a été mis à jour.")
        else:
            raise ValueError(
                f"Match avec l'ID {match.id} introuvable ou aucune modification effectuée.")