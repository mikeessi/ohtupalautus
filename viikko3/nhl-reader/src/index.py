import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.response = requests.get(url).json()
        self.players = self.create_players()

    def create_players(self):
        players = []
        for player_dict in self.response:
            player = Player(
               player_dict['name'],
               player_dict['nationality'],
               player_dict['team'],
               player_dict['goals'],
               player_dict['assists']
            )
            players.append(player)
        return players

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        self.players = self.reader.players

    def top_scorers_by_nationality(self, nationality):
        nat_players = [player for player in self.players if player.nationality == nationality]
        nat_players.sort(reverse=True,key = lambda player: player.points)
        return nat_players

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)


if __name__ == "__main__":
    main()
