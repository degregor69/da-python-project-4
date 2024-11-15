import datetime
from models.tournaments.tournaments_manager import TournamentsManager


def create_tournament():
    print("Création d'un tournoi")
    name = input("Nom du tournoi : ")
    location = input("Lieu du tournoi : ")

    start_date = get_date("Date de début (JJ/MM/AAAA) : ")
    end_date = get_date("Date de fin (JJ/MM/AAAA) : ")

    nb_rounds = get_nb_rounds("Nombre de rounds (par défaut 4) :  ")

    description = input("Remarques du directeur : ")

    return {
        "name": name,
        "location": location,
        "start_date": start_date,
        "end_date": end_date,
        "nb_rounds": nb_rounds,
        "description": description,
    }


def ask_for_players(tournament_manager: TournamentsManager):
    print("Liste des jours enregistrés :")
    db_players = tournament_manager.get_players()
    while True:
        selection = input(
            'Pour sélectionner un joueur, entrez son ID national, sinon entrez "STOP"'
        )
        if selection == "STOP":
            break
        


def get_date(prompt: str) -> datetime.date:
    while True:
        try:
            date_str = input(prompt)
            return datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
        except ValueError:
            print("Format de date invalide. Veuillez réessayer.")


def get_nb_rounds(prompt: str):
    nb_rounds_input = input(prompt)
    if nb_rounds_input == "":
        return 4
    return int(nb_rounds_input)
