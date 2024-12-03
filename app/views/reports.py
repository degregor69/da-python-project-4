from models.players.players import Player
from models.tournaments.tournaments import Tournament


class ReportsViews:
    @staticmethod
    def reports_selection():
        while True:
            print("Choisissez l'option que vous convient : ")
            print("1. Liste de tous les joueurs par ordre alphabétique")
            print("2. Liste de tous les tournois")
            selection = input("\nChoisissez une option : ")
            if selection in ["1", "2"]:
                return int(selection)
            print(
                "Sélection invalide, veuillez sélectionner une option parmi la liste."
            )

    @staticmethod
    def display_players(players: list[Player]):
        for player in players:
            print(f"Nom : {player.full_name} | Date de naissance : {player.birth_date}")

    @staticmethod
    def display_tournament_details(tournament: Tournament):
        print("Voici les détails du tournoi :")
        print(f"Nom : {tournament.name}")
        print(
            f"Date de début : {tournament.start_date} | Date de fin : {tournament.end_date}"
        )
        print("\nListe des joueurs par ordre alphabétique :")
        sorted_players = sorted(tournament.players, key=lambda player: player.full_name)
        ReportsViews.display_players(sorted_players)
        print("\nListe des tours :")
        for round in tournament.rounds:
            print(f"\nTour : {round.name}")
            print(
                f"Date de début : {round.start_datetime.strftime('%d/%m/%Y à %H:%M')} | "
                f"Date de fin : {round.end_datetime.strftime('%d/%m/%Y à %H:%M')}"
            )
            print("\nMatchs du round : ")
            for match in round.matches:
                print(
                    f"{match.player_1.national_id} | {match.score_player_1} vs "
                    f"{match.player_2.national_id} | {match.score_player_2}"
                )
