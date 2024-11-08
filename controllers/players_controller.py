import datetime
import re


class PlayerController:
    def __init__(self, db):
        self.db = db.table('players')
        self.players = []  # Liste pour stocker les joueurs

    def add_player(self):
        print("Ajoutons un joueur !")
        last_name = input("Nom de famille : ")
        first_name = input("Prénom : ")
        birth_date = input("Date de naissance (JJ/MM/AAAA) : ")
        national_id = input("ID national : ")

        # Validation de la date
        if not self._validate_date(birth_date):
            print("Erreur : La date de naissance n'est pas valide.")
            return

        # Validation de l'id national
        if not self._validate_national_id(national_id):
            print("Erreur : l'id national n'est pas au bon format.")
            return

        player_data = {
            'last_name': last_name,
            'first_name': first_name,
            'birth_date': birth_date,
            'national_id': national_id,
            'points': 0.0
        }
        self.db.insert(player_data)  # Insertion dans TinyDB
        print(f"Le joueur {first_name} {last_name} a été ajouté avec succès !")

    @staticmethod
    def _validate_date(date_text):
        try:
            datetime.datetime.strptime(date_text, "%d/%m/%Y")
            return True
        except ValueError:
            return False

    @staticmethod
    def _validate_national_id(national_id):
        # Exemple : ID sous forme de deux lettres suivies de 6 chiffres
        if re.match(r"^[A-Z]{2}\d{6}$", national_id):
            return True
        else:
            return False