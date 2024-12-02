def check_if_player_already_registered(
    registered_players: list[str], players: list[str], national_id: str
):
    if national_id in registered_players:
        print(f"Le joueur {national_id} est déjà inscrit à ce tournoi.")
        return

    if national_id not in players:
        print("Aucun joueur avec cet ID n'a été retrouvé.")
        return

    return national_id
