from controllers.players_controller import PlayerController
from data.database import players_db


class MainController:
    def __init__(self):
        self.player_controller = PlayerController(players_db)

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
                break
            # elif choice == '2':
            #     create_tournament()
            # elif choice == '3':
            #     start_round()
            # elif choice == '4':
            #     show_reports()
            # elif choice == '5':
            #     print("Au revoir !")
            #     break
            else:
                print("Option invalide. Veuillez réessayer.")

