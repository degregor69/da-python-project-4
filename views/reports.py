from models.players.players import Player


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
            print("Sélection invalide, veuillez sélectionner une option parmi la liste.")

    @staticmethod
    def display_players(players: list[Player]):
        for player in players:
            print(f"Nom : {player.full_name} | Date de naissance : {player.birth_date} | Points : {player.points}")