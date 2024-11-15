import datetime

from models.players.players_manager import PlayersManager
from models.tournaments.tournaments_manager import TournamentsManager
from controllers.create_tournaments_controller import CreateTournamentController


def get_tournament(tournament_manager: TournamentsManager):
    all_tournaments = tournament_manager.get_all_tournaments()
    print("Choisissez le tournoi à lancer ou reprendre :")
    for tournament in all_tournaments:
        print(
            f"{tournament.name} | {tournament.location} | {tournament.start_date} | {tournament.end_date} "
        )


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


def ask_for_players(
    tournament_manager: TournamentsManager, players_manager: PlayersManager
):
    registered_players: list[str] = []
    print("Liste des jours enregistrés :")
    players = players_manager.get_all_players()
    players_ids = [player.national_id for player in players]
    for player in players:
        print(f"{player.national_id} | {player.first_name} {player.last_name}")
    while True:
        selection = input(
            'Pour sélectionner un joueur, entrez son ID national, sinon entrez "STOP"'
        )
        if selection == "STOP":
            break
        player = CreateTournamentController.check_if_player_already_registered(
            registered_players, players_ids, selection
        )
        if player:
            registered_players.append(player)

    print("Joueurs inscrits au tournoi :")
    for registered_player in registered_players:
        print(
            f"{registered_player}"
        )
    return registered_players


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
