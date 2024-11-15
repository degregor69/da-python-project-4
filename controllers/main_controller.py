from controllers.players_controller import PlayerController
from controllers.tournaments_controller import TournamentController


class MainController:
    def __init__(self):
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentController()

    def run(self):
        print("Bienvenue au gestionnaire de tournoi d'échecs !")
        while True:
            print("\nMenu principal")
            print("1. Ajouter un joueur")
            print("2. Créer un tournoi")
            print("3. Lancer un tour")
            print("4. Afficher les rapports")
            print("5. Quitter")

            choice = input("Choisissez une option : ")

            if choice == '1':
                self.player_controller.add_player()
            elif choice == '2':
                self.tournament_controller.create_tournament()
            # elif choice == '3':
            #     start_round()
            # elif choice == '4':
            #     show_reports()
            elif choice == '5':
                print("Au revoir !")
                break
            else:
                print("Option invalide. Veuillez réessayer.")
