from random import randint

class Die:
    """Used to model a die of any D size."""

    def __init__(self, num_sides=6):
        """initilizes the oinstance itself with the atts it needs for creating a die."""
        self.num_sides = num_sides

    def roll_die(self):
        """Used to roll the die and get random num."""
        roll = randint(1, self.num_sides)
        return roll