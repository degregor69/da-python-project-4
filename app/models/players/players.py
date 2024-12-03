import datetime


class Player:
    def __init__(
        self,
        last_name: str,
        first_name: str,
        birth_date: datetime.date,
        national_id: str,
    ):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.national_id = national_id

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
            "national_id": self.national_id,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            last_name=data["last_name"],
            first_name=data["first_name"],
            birth_date=datetime.datetime.strptime(
                data["birth_date"], "%d/%m/%Y"
            ).date(),
            national_id=data["national_id"],
        )
