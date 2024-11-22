import datetime
import utils
from models.players.players import Player
from models.players.players_manager import PlayersManager
from models.rounds.rounds import Round
from models.tournaments.tournaments_manager import TournamentsManager


class CreateTournamentViews:
    @staticmethod
    def create_tournament():
        print("Création d'un tournoi")
        name = input("Nom du tournoi : ")
        location = input("Lieu du tournoi : ")
        start_date = CreateTournamentViews.get_date("Date de début (JJ/MM/AAAA) : ")
        end_date = CreateTournamentViews.get_date("Date de fin (JJ/MM/AAAA) : ")
        nb_rounds = CreateTournamentViews.get_nb_rounds(
            "Nombre de rounds (par défaut 4) :  "
        )
        description = input("Remarques du directeur : ")

        return {
            "name": name,
            "location": location,
            "start_date": start_date,
            "end_date": end_date,
            "nb_rounds": nb_rounds,
            "description": description,
        }

    @staticmethod
    def ask_for_players(
        tournament_manager: TournamentsManager, players_manager: PlayersManager
    ):
        registered_players = []
        print("Liste des joueurs enregistrés :")
        players = players_manager.get_all_players()
        players_ids = [player.national_id for player in players]

        for player in players:
            print(f"{player.national_id} | {player.first_name} {player.last_name}")

        while True:
            selection = input(
                'Pour sélectionner un joueur, entrez son ID national, sinon entrez "STOP" : '
            )
            if selection == "STOP":
                break

            player = utils.check_if_player_already_registered(
                registered_players, players_ids, selection
            )
            if player:
                registered_players.append(player)

        print("Joueurs inscrits au tournoi :")
        for registered_player in registered_players:
            print(f"{registered_player}")
        return registered_players

    @staticmethod
    def get_date(prompt: str) -> datetime.date:
        while True:
            try:
                date_str = input(prompt)
                return datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
            except ValueError:
                print("Format de date invalide. Veuillez réessayer.")

    @staticmethod
    def get_nb_rounds(prompt: str):
        nb_rounds_input = input(prompt)
        if nb_rounds_input == "":
            return 4
        return int(nb_rounds_input)


class StartTournamentViews:
    @staticmethod
    def select_tournament(tournament_manager: TournamentsManager):
        all_tournaments = tournament_manager.get_all_tournaments()
        print("Choisissez le tournoi à lancer ou reprendre :")
        for index, tournament in enumerate(all_tournaments):
            print(
                f"{index + 1} - {tournament.name} | {tournament.location} | {tournament.start_date} | {tournament.end_date}"
            )
        choice = input("Entrez le numéro du tournoi : ")
        if choice.isdigit() and 1 <= int(choice) <= len(all_tournaments):
            return all_tournaments[int(choice) - 1]
        else:
            print("Choix invalide.")
            return None

    @staticmethod
    def display_tournament_actual_round(actual_round: int):
        if actual_round == 0:
            print(f"Début du tournoi, round {actual_round}")
        else:
            print(f"Reprise du tournoi, round {actual_round}")

    @staticmethod
    def display_tournament_players(players: list[Player]):
        players_names = [f"{player.first_name} {player.last_name}" for player in players]
        players_str = ", ".join(players_names)
        print(f"Les joueurs participants à ce tournoi : {players_str}.")

    @staticmethod
    def display_sorted_players(sorted_players: list[Player]):
        players_names = [f"{player.first_name} {player.last_name}" for player in sorted_players]
        players_str = ", ".join(players_names)
        print(f"Les joueurs ont été triés aléatoirement dans cet ordre : {players_str}.")

    @staticmethod
    def display_created_round(round: Round):
        print(f"Le round a été créé.")
        print(f"Les matchs qui le composent sont : ")
        for match in round.matches:
            print(f"{match.player_1.national_id} | {match.player_1.first_name} {match.player_1.last_name} VS {match.player_2.national_id} | {match.player_2.first_name} {match.player_2.last_name}")