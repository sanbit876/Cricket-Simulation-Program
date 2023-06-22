"""
    Class Representing the umpire who officiates the match and keeps track of scores, wickets, and overs.

    Attributes:
        scores (int): The total score of the batting team.
        wickets (int): The number of wickets taken by the bowling team.
        overs (int): The number of overs bowled.
    """

class Umpire:
    def __init__(self):
        self.scores = 0
        self.wickets = 0
        self.overs = 0

    def predict_outcome(self, batsman):
        return batsman.play_ball()

    def update_score(self, runs):
        self.scores += runs

    def update_wicket(self):
        self.wickets += 1

    def update_over(self):
        self.overs += 1
