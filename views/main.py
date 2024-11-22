class MainControllerViews:
    @staticmethod
    def main_menu():
        print("\nBienvenue au gestionnaire de tournoi d'échecs !")
        print("\nMenu principal")
        print("1. Ajouter un joueur")
        print("2. Créer un tournoi")
        print("3. Lancer un tour")
        print("4. Afficher les rapports")
        print("5. Quitter")

        choice = input("Choisissez une option : ")
        return choice

    @staticmethod
    def goodbye():
        print("Au revoir !")

    @staticmethod
    def error():
        print("Option invalide. Veuillez réessayer.")