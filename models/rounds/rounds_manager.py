from tinydb import TinyDB, Query

from models.matches.matches_manager import MatchesManager
from models.rounds.rounds import Round

class RoundsManager:
    def __init__(self, db_path="data/rounds.json"):
        self.db = TinyDB(db_path).table("rounds")
        self._id_counter = self._get_next_id()
        self.matches_manager = MatchesManager()

    def _get_next_id(self):
        """Charge l'ID suivant en examinant la base de données"""
        if len(self.db) > 0:
            last_round = self.db.all()[-1]  # Récupère le dernier round enregistré
            return last_round["id"] + 1  # Incrémente de 1 l'ID du dernier round
        return 1  # Si la base est vide, commence à 1

    def add_round(self, round: Round):
        """Ajoute un round à la base de données avec un ID unique"""
        if round.id is None:
            round.id = self._id_counter  # Attribue l'ID unique du compteur
            self._id_counter += 1  # Incrémente le compteur pour le prochain round
        self.db.insert(round.to_dict())  # Sauvegarde le round dans la base de données

    def get_round(self, round_id):
        """Récupère un round depuis la base de données par son ID"""
        round_data = self.db.get(Query().id == round_id)
        if round_data:
            return Round.from_dict(round_data, self.matches_manager)  # Récupère le round avec les matchs
        return None
