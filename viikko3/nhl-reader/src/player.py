class Player:
    def __init__(self, name, nationality, team, goals, assists):
        self.name = name
        self.nationality = nationality
        self.team = team
        self.goals = goals
        self.assists = assists
        self.points = self.goals + self.assists

    def __str__(self):
        return f"{self.name:20} {self.team} {str(self.goals).rjust(2)} + {str(self.assists).rjust(2)} = {str(self.points).rjust(2)}"
