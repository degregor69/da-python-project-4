from controllers.add_players_controller import AddPlayerController
from controllers.create_tournaments_controller import CreateTournamentController
from controllers.start_tournament_controller import StartTournamentController


class MainController:
    def __init__(self):
        self.player_controller = AddPlayerController()
        self.create_tournament_controller = CreateTournamentController()
        self.start_tournament_controller = StartTournamentController()

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

            if choice == "1":
                self.player_controller.run()
            elif choice == "2":
                self.create_tournament_controller.run()
            elif choice == "3":
                self.start_tournament_controller.run()
            # elif choice == '4':
            #     show_reports()
            elif choice == "5":
                print("Au revoir !")
                break
            else:
                print("Option invalide. Veuillez réessayer.")
