import datetime
import re
from views.players import AddPlayerViews
from models.players.players import Player
from models.players.players_manager import PlayersManager


class AddPlayerController:
    def __init__(self):
        self.players_manager = PlayersManager()

    def run(self):
        new_player_dict = AddPlayerViews.get_player_data()
        new_player = Player(**new_player_dict)

        if not self._validate_date(new_player.birth_date):
            AddPlayerViews.birthdate_error()
            return

        if not self._validate_national_id(new_player.national_id):
            AddPlayerViews.national_id_error()
            return

        self.players_manager.add_player(new_player)

        AddPlayerViews.display_added_player_message(
            new_player.first_name, new_player.last_name
        )

    @staticmethod
    def _validate_date(date_text):
        try:
            datetime.datetime.strptime(date_text, "%d/%m/%Y")
            return True
        except ValueError:
            return False

    @staticmethod
    def _validate_national_id(national_id):
        # Id must be two letters followed by 5 digits
        if re.match(r"^[A-Z]{2}\d{5}$", national_id):
            return True
        else:
            return False
