"""
    Class Representing the commentator who provides live commentary of the match.

    Attributes:
        None
    """

import time

class Commentator:
    def __init__(self):
        pass

    def comment(self, event):
        time.sleep(1)  # Add a 1-second delay between statements
        print(event)
