"""
    Class Representing a cricket team with players.

    Attributes:
        name (str): The name of the team.
        players (list): List of players in the team.
        captain (Player): The captain of the team.
        batting_order (list): The batting order of the team.
    """

import random

class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.captain = None
        self.batting_order = []

    def select_captain(self, player):
        self.captain = player

    def send_next_player(self):

        # Select the next player based on batting order logic

        if not self.batting_order:
            self.batting_order = self.players.copy()
            random.shuffle(self.batting_order)
        return self.batting_order.pop(0)

    def choose_bowler(self):

        # Select the bowler for an over based on bowling order logic

        return random.choice(self.players)
