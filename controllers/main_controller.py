from controllers.add_players_controller import AddPlayerController
from controllers.create_tournaments_controller import CreateTournamentController
from controllers.start_tournament_controller import StartTournamentController
from views.main import MainControllerViews


class MainController:
    def __init__(self):
        self.player_controller = AddPlayerController()
        self.create_tournament_controller = CreateTournamentController()
        self.start_tournament_controller = StartTournamentController()

    def run(self):
        while True:
            choice = MainControllerViews.main_menu()
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
