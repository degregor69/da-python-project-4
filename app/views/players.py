class AddPlayerViews:
    @staticmethod
    def get_player_data():
        print("Ajoutons un joueur !")
        last_name = input("Nom de famille : ")
        first_name = input("Prénom : ")
        birth_date = input("Date de naissance (JJ/MM/AAAA) : ")
        national_id = input("ID national : ")
        return {
            "last_name": last_name,
            "first_name": first_name,
            "birth_date": birth_date,
            "national_id": national_id,
        }

    @staticmethod
    def display_added_player_message(first_name, last_name):
        print(f"\nLe joueur {first_name} {last_name} a été ajouté avec succès !")

    @staticmethod
    def birthdate_error():
        print("Erreur : La date de naissance n'est pas valide.")

    @staticmethod
    def national_id_error():
        print("Erreur : l'id national n'est pas au bon format.")
