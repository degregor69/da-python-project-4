from tinydb import TinyDB, Query

from app.models.matches.matches_manager import MatchesManager
from app.models.rounds.rounds import Round


class RoundsManager:
    def __init__(self, db_path="data/rounds.json"):
        self.db = TinyDB(db_path).table("rounds")
        self._id_counter = self._get_next_id()
        self.matches_manager = MatchesManager()

    def _get_next_id(self):
        if len(self.db) > 0:
            last_round = self.db.all()[-1]  # Get last registered
            return last_round["id"] + 1  # Add 1 to its id
        return 1  # if db empty return 1 because first one to be saved

    def add_round(self, round: Round):
        if round.id is None:
            round.id = self._id_counter  # Attribue l'ID unique du compteur
            self._id_counter += 1  # Incrémente le compteur pour le prochain round
        # Sauvegarde le round dans la base de données
        self.db.insert(round.to_dict())

    def get_round(self, round_id):
        round_data = self.db.get(Query().id == round_id)
        if round_data:
            # Récupère le round avec les matchs
            return Round.from_dict(round_data, self.matches_manager)
        return None

    def update_round(self, round: Round):
        RoundQuery = Query()
        round_data = round.to_dict()
        self.db.update(round_data, RoundQuery.id == round.id)
