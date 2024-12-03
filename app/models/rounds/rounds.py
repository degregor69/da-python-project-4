import datetime
from typing import List, Optional

from models.matches.matches import Match
from models.matches.matches_manager import MatchesManager


class Round:
    def __init__(
        self,
        name: str,
        matches: List[Match],
        start_datetime: datetime.datetime = datetime.datetime.now(),
        id: Optional[int] = None,
        end_datetime: Optional[datetime.datetime] = None,
    ):
        self.id = id
        self.name = name
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.matches = matches

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "start_datetime": self.start_datetime.isoformat(),
            "end_datetime": self.end_datetime.isoformat()
            if self.end_datetime
            else None,
            "matches": [match.id for match in self.matches],
        }

    @classmethod
    def from_dict(cls, data: dict, matches_manager: MatchesManager):
        # On récupère les objets Match via le MatchesManager
        matches = [matches_manager.get_match(match_id) for match_id in data["matches"]]
        return cls(
            id=data["id"],
            name=data["name"],
            start_datetime=datetime.datetime.fromisoformat(data["start_datetime"]),
            end_datetime=datetime.datetime.fromisoformat(data["end_datetime"])
            if data["end_datetime"]
            else None,
            matches=matches,  # Associe les objets Match
        )
