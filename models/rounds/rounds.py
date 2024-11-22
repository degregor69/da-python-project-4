import datetime
from typing import List

class Round:
    _id_counter = 1  # Variable de classe pour suivre le prochain ID

    def __init__(
        self,
        name: str,
        end_datetime: datetime.datetime,
        matches: List[int],  # Liste d'IDs (int) des matchs
        start_datetime: datetime.datetime = datetime.datetime.now(),
    ):
        self.id = Round._id_counter  # Attribuer un ID unique au round
        Round._id_counter += 1  # Incrémenter le compteur pour le prochain round
        self.name = name
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.matches = matches

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "start_datetime": self.start_datetime.isoformat(),
            "end_datetime": self.end_datetime.isoformat(),
            "matches": self.matches,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data["name"],
            start_datetime=datetime.datetime.fromisoformat(data["start_datetime"]),
            end_datetime=datetime.datetime.fromisoformat(data["end_datetime"]),
            matches=data["matches"],
        )
