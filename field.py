"""
    Class Representing the cricket field and its conditions.

    Attributes:
        size (str): The size of the field.
        fan_ratio (float): The fan ratio or crowd support.
        pitch_conditions (str): The conditions of the pitch.
        home_advantage (float): The home advantage factor.
    """

class Field:
    def __init__(self, size, fan_ratio, pitch_conditions, home_advantage):
        self.size = size
        self.fan_ratio = fan_ratio
        self.pitch_conditions = pitch_conditions
        self.home_advantage = home_advantage
