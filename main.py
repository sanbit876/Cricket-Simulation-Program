import random
import time
from player import Player
from team import Team
from field import Field
from umpire import Umpire
from commentator import Commentator
from match import Match

def main():
    player1 = Player("MS Dhoni", {'batting': 0.8, 'bowling': 0.2, 'fielding': 0.99, 'running': 0.8, 'experience': 0.9})
    player2 = Player("Virat Kohli", {'batting': 0.85, 'bowling': 0.15, 'fielding': 0.95, 'running': 0.75, 'experience': 0.95})
    player3 = Player("Rohit Sharma", {'batting': 0.9, 'bowling': 0.1, 'fielding': 0.9, 'running': 0.8, 'experience': 0.9})
    team1 = Team("Team 1", [player1, player2, player3])

    player4 = Player("Kane Williamson", {'batting': 0.8, 'bowling': 0.2, 'fielding': 0.99, 'running': 0.8, 'experience': 0.9})
    player5 = Player("Steve Smith", {'batting': 0.85, 'bowling': 0.15, 'fielding': 0.95, 'running': 0.75, 'experience': 0.95})
    player6 = Player("Joe Root", {'batting': 0.9, 'bowling': 0.1, 'fielding': 0.9, 'running': 0.8, 'experience': 0.9})
    team2 = Team("Team 2", [player4, player5, player6])

    field = Field("Large", 0.8, "Dry", 0.1)

    match = Match(team1, team2, field)
    match.simulate_match()


if __name__ == "__main__":
    main()