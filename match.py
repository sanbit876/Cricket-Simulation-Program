"""
    Class Representing a cricket match between two teams.

    Attributes:
        team1 (Team): The first team in the match.
        team2 (Team): The second team in the match.
        field (Field): The field and its conditions for the match.
        umpire (Umpire): The umpire officiating the match.
        commentator (Commentator): The commentator providing live commentary.
    """

import random
from umpire import Umpire
from commentator import Commentator

class Match:
    def __init__(self, team1, team2, field):
        self.team1 = team1
        self.team2 = team2
        self.field = field
        self.umpire = Umpire()
        self.commentator = Commentator()

    def simulate_match(self):
        # Simulate the cricket match
        self.start_match()
        self.play_innings(self.team1, self.team2)
        self.play_innings(self.team2, self.team1)
        self.end_match()

    def start_match(self):
        self.commentator.comment("The match has started!")

    def play_innings(self, batting_team, bowling_team):
        self.commentator.comment(f"{batting_team.name} is now batting.")

        for _ in range(50):  # Assuming 50 overs per team
            self.commentator.comment(f"Over {_ + 1} begins.")
            for _ in range(6):  # 6 balls per over
                batsman = batting_team.send_next_player()
                bowler = bowling_team.choose_bowler()

                outcome = self.umpire.predict_outcome(batsman)

                if outcome == "Boundary":
                    self.umpire.update_score(4)
                    self.commentator.comment(f"{batsman.name} hits a boundary!")
                else:
                    self.umpire.update_wicket()
                    self.commentator.comment(f"{batsman.name} is out!")

                self.umpire.update_over()

            self.commentator.comment(
                f"Over {_ + 1} ends. {batting_team.name} score: {self.umpire.scores}/{self.umpire.wickets}"
            )

            # Check for innings break or target chase

            if self.umpire.scores > 300:  # Modify the logic based on target or innings break conditions
                self.commentator.comment(
                    f"{batting_team.name} has set a target of {self.umpire.scores + 1} runs."
                )
                break

        self.commentator.comment(
            f"{batting_team.name} innings ends with a total of {self.umpire.scores}/{self.umpire.wickets}."
        )

    def end_match(self):
        self.commentator.comment("The match has ended.")
