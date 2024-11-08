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

        player_data = {
            'last_name': last_name,
            'first_name': first_name,
            'birth_date': birth_date,
            'national_id': national_id,
            'points': 0.0
        }
        self.db.insert(player_data)  # Insertion dans TinyDB
        print(f"Le joueur {first_name} {last_name} a été ajouté avec succès !")