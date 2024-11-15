import datetime

from models.players.players import Player
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
    registered_players = []
    print("Liste des jours enregistrés :")
    players = tournament_manager.get_all_players()
    for player in players:
        print(f"{player.national_id} | {player.first_name} {player.last_name}")
    while True:
        selection = input(
            'Pour sélectionner un joueur, entrez son ID national, sinon entrez "STOP"'
        )
        if selection == "STOP":
            break
        player = find_player_by_national_id(registered_players, players, selection)
        if player:
            registered_players.append(player)

    print("Joueurs inscrits au tournoi :")
    for registered_player in registered_players:
        print(
            f"{registered_player.first_name} {registered_player.last_name} {registered_player.national_id}"
        )
    return registered_players


def find_player_by_national_id(
    registered_players: list[Player], players: list[Player], national_id: str
):
    matching_player = [
        player for player in registered_players if player.national_id == national_id
    ]
    if matching_player:
        print(
            f"Le joueur {matching_player[0].first_name} {matching_player[0].last_name} est déjà inscrit à ce tournoi."
        )
        return

    for player in players:
        if player.national_id == national_id:
            return player
    print("Aucun joueur avec cet ID n'a été retrouvé.")
    return


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
