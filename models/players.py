class Player:
    def __init__(self, last_name: str, first_name: str, birth_date: str, national_id: str):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.national_id = national_id
        self.points = 0.0  # Score initial du joueur pour les tournois

    def add_points(self, points: float):
        self.points += points