from tinydb import TinyDB, Query
from app.models.players.players import Player


class PlayersManager:
    def __init__(self, db_path="data/players.json"):
        self.db = TinyDB(db_path).table("players")

    def add_player(self, player: Player):
        self.db.insert(player.__dict__)

    def get_player(self, player_id: str):
        PlayerQuery = Query()
        player_data = self.db.get(PlayerQuery.national_id == player_id)
        if player_data:
            return Player.from_dict(player_data)
        return

    def get_all_players(self):
        players_data = self.db.all()
        return [Player.from_dict(data) for data in players_data]

    def get_all_players_ids(self):
        players = self.get_all_players()
        return [player.national_id for player in players]

    def update_player(self, player):
        PlayerQuery = Query()
        self.db.update(
            player.to_dict(),
            PlayerQuery.national_id == player.national_id)
