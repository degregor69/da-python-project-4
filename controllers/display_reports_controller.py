from models.players.players_manager import PlayersManager
from views.reports import ReportsViews


class DisplayReportsController:
    def __init__(self):
        self.players_manager = PlayersManager()

    def run(self):
        selection = ReportsViews.reports_selection()
        if selection == 1: # Display all player by alphabetical order
            self.display_players_by_alphabetical_order()


    def display_players_by_alphabetical_order(self):
        players = self.players_manager.get_all_players()
        sorted_players = sorted(players, key=lambda player: player.full_name)
        ReportsViews.display_players(sorted_players)