class Player:
    def __init__(self, last_name: str, first_name: str, birth_date: str, national_id: str):
        """
        Initialise un nouveau joueur avec son nom, prénom, date de naissance, et identifiant national d'échecs.

        :param last_name: Nom de famille du joueur
        :param first_name: Prénom du joueur
        :param birth_date: Date de naissance du joueur au format 'YYYY-MM-DD'
        :param national_id: Identifiant national d'échecs (format AB12345)
        """
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.national_id = national_id
        self.points = 0.0  # Score initial du joueur pour les tournois