from models.matches.matches import Match


class MatchesViews:

    @staticmethod
    def set_match_score(match: Match):
        print(
            f"\nQuelle est l'issue du match {match.id} opposant : {match.player_1.national_id} | {match.player_1.first_name} {match.player_1.last_name} à {match.player_2.national_id} | {match.player_2.first_name} {match.player_2.last_name} ?")
        print(f"1. Victoire de {match.player_1.national_id}")
        print(f"2. Victoire de {match.player_2.national_id}")
        print(f"3. Match nul")

        while True:
            try:
                choice = int(input("\nEntrez le numéro de l'issue du match (1, 2 ou 3) : "))
                if choice in [1, 2, 3]:
                    return choice
                else:
                    print("\nChoix invalide. Veuillez entrer 1, 2 ou 3.")
            except ValueError:
                print("\nEntrée invalide. Veuillez entrer un nombre (1, 2 ou 3).")
