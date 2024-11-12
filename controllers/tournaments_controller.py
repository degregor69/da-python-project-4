import datetime
from tinydb import TinyDB, Query

from models.tournaments import Tournament


class TournamentController:
    def __init__(self, tournaments_db, players_db):
        self.db = tournaments_db  # Base de données pour les tournois
        self.players_db = players_db  # Base de données pour les joueurs

    def create_tournament(self):
        # # Demander les informations nécessaires pour créer un tournoi
        # print("Création d'un tournoi")
        # name = input("Nom du tournoi : ")
        # location = input("Lieu du tournoi : ")
        #
        # # Validation des dates de début et de fin
        # start_date = self.get_date("Date de début (JJ/MM/AAAA) : ")
        # end_date = self.get_date("Date de fin (JJ/MM/AAAA) : ")
        #
        # # Demande du nombre de rounds
        # nb_rounds = self.get_nb_rounds("Nombre de rounds (par défaut 4) :  ")
        #
        # print(name, location, start_date, end_date, nb_rounds)

        # Choisir les joueurs à ajouter au tournoi
        players = self.get_players()
        #
        # # Créer le tournoi
        # tournament = Tournament(name, location, start_date, end_date, players)
        #
        # # Sauvegarder le tournoi dans la base de données
        # self.save_tournament(tournament)
        #
        # print(f"Tournoi '{name}' créé avec succès !")

    def get_date(self, prompt: str) -> datetime.date:
        while True:
            try:
                date_str = input(prompt)
                return datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
            except ValueError:
                print("Format de date invalide. Veuillez réessayer.")

    def get_nb_rounds(self, prompt: str):
        nb_rounds_input = input(prompt)
        if nb_rounds_input == "":
            return 4
        return int(nb_rounds_input)

    def get_players(self):
        players = []
        print("Sélectionnez les joueurs pour le tournoi : ")
        # Récupérer la liste des joueurs dans la base de données
        db_players = self.players_db.table("players").all()
        for db_player in db_players:
            print(f"{db_player['national_id']} {db_player['first_name']} {db_player['last_name']}")




    def save_tournament(self, tournament: Tournament):
        # Sauvegarder le tournoi dans la base de données
        self.db.insert({
            'name': tournament.name,
            'location': tournament.location,
            'start_date': str(tournament.start_date),
            'end_date': str(tournament.end_date),
            'players': tournament.players,
            'nb_rounds': tournament.nb_rounds
        })

