from models.tournaments.tournaments_manager import TournamentsManager
from models.tournaments.tournaments import Tournament
from views import tournaments as tournaments_views


class TournamentController:
    def __init__(self):
        self.tournaments_manager = TournamentsManager()

    def create_tournament(self):
        new_tournament_as_dict = tournaments_views.create_tournament()
        new_tournament = Tournament(**new_tournament_as_dict)

        # Sélection des joueurs
        tournaments_views.ask_for_players(self.tournaments_manager)

        # # Créer le tournoi
        # tournament = Tournament(name, location, start_date, end_date, players)
        #
        # # Sauvegarder le tournoi dans la base de données
        # self.save_tournament(tournament)
        #
        # print(f"Tournoi '{name}' créé avec succès !")

    def save_tournament(self, tournament: Tournament):
        # Sauvegarder le tournoi dans la base de données
        self.db.insert(
            {
                "name": tournament.name,
                "location": tournament.location,
                "start_date": str(tournament.start_date),
                "end_date": str(tournament.end_date),
                "players": tournament.players,
                "nb_rounds": tournament.nb_rounds,
            }
        )
