from app.models.players.players_manager import PlayersManager
from app.models.tournaments.tournaments_manager import TournamentsManager
from app.views.reports import ReportsViews
from app.views.tournaments import StartTournamentViews


class DisplayReportsController:
    def __init__(self):
        self.players_manager = PlayersManager()
        self.tournaments_manager = TournamentsManager()

    def run(self):
        selection = ReportsViews.reports_selection()
        if selection == 1:  # Display all players by alphabetical order
            self.display_players_by_alphabetical_order()
        if selection == 2:  # Display all tournaments
            all_tournaments = self.tournaments_manager.get_all_tournaments()
            tournament = StartTournamentViews.select_tournament(
                all_tournaments)
            ReportsViews.display_tournament_details(tournament)

    def display_players_by_alphabetical_order(self):
        players = self.players_manager.get_all_players()
        sorted_players = sorted(players, key=lambda player: player.full_name)
        ReportsViews.display_players(sorted_players)
