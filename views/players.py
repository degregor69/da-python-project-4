def add_player():
        print("Ajoutons un joueur !")
        last_name = input("Nom de famille : ")
        first_name = input("Prénom : ")
        birth_date = input("Date de naissance (JJ/MM/AAAA) : ")
        national_id = input("ID national : ")
        return {"last_name": last_name, "first_name": first_name, "birth_date": birth_date, "national_id": national_id}