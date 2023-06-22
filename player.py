"""
    Class Representing a cricket player with various stats.

    Attributes:
        name (str): The name of the player.
        stats (dict): The player's statistics, such as batting, bowling, fielding, running, and experience.
    """

import random

class Player:
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats

    def play_ball(self):

        # Simulate player's performance on a ball
        # Modify the logic based on player's stats and probabilities

        batting_prob = self.stats.get('batting', 0.5)
        if random.random() < batting_prob:
            return "Boundary"
        else:
            return "Out"
