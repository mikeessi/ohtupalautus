import unittest
from statistics import Statistics, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(
            PlayerReaderStub()
        )


    def test_search_player_who_doesnt_exist(self):
        player = self.statistics.search("Selanne")
        self.assertEqual(player, None)

    def test_search_player_who_exists(self):
        player = self.statistics.search("Semenko")
        self.assertEqual(player.name, "Semenko" )

    def test_team_return_list(self):
        players = self.statistics.team("DET")
        player = players[0]
        self.assertEqual(player.name, "Yzerman")

    def test_top_highest_points_first(self):
        players = self.statistics.top(3)
        top_scorer = players[0]
        self.assertEqual(top_scorer.name, "Gretzky")

    def test_top_highest_assists_first(self):
        players = self.statistics.top(3, SortBy.ASSISTS)
        top_scorer = players[0]
        self.assertEqual(top_scorer.name, "Gretzky")

    def test_top_highest_goals_first(self):
        players = self.statistics.top(3, SortBy.GOALS)
        top_scorer = players[0]
        self.assertEqual(top_scorer.name, "Lemieux")
