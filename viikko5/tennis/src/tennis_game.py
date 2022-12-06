class TennisGame:

    def __init__(self, player1_name, player2_name):
        self.player1 = player1_name
        self.player2 = player2_name
        self.p1_score = 0
        self.p2_score = 0

    def won_point(self, player):
        if player == self.player1:
            self.p1_score += 1
        else:
            self.p2_score += 1

    def get_score(self):

        if self.p1_score == self.p2_score:
            score = self.get_score_tied(self.p1_score)
        elif self.p1_score >= 4 or self.p2_score >= 4:
            difference = self.p1_score - self.p2_score
            score = self.get_score_four_or_more(difference)
        else:
            score = f"{self.get_score_string(self.p1_score)}-{self.get_score_string(self.p2_score)}"
        return score

    def get_score_tied(self, score):
        if score == 0:
            return "Love-All"
        if score == 1:
            return "Fifteen-All"
        if score == 2:
            return "Thirty-All"
        if score == 3:
            return "Forty-All"
        return "Deuce"

    def get_score_string(self, score):
        if score == 0:
            return "Love"
        if score == 1:
            return "Fifteen"
        if score == 2:
            return "Thirty"
        if score == 3:
            return "Forty"

    def get_score_four_or_more(self, difference):
         if difference == 1:
             return f"Advantage {self.player1}"
         if difference >= 2:
             return f"Win for {self.player1}"
         if difference == -1:
             return f"Advantage {self.player2}"
         if difference <= -2:
             return f"Win for {self.player2}"
