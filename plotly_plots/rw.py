from random import choice

class RandomWalk:
    """Used to model a random walk. Random walks appear through many things in life. One example
    is a grain of pollen floating on a water droplet. Not moving in any particular formation. Just
    mving at the mercy of fate."""

    def __init__(self, points=5000):
        """Initilizes the instance of an obj when called to assign its atts."""
        self.points = points

        # need the zero to avoid the indexing error
        self.x_points = [0]
        self.y_points = [0]

    def run_walk(self):
        """Used to run the walk portion and generate our data of points randomlt generated
        through the method choice."""
        while len(self.x_points) < self.points:
            # we forgot to run _step() function directly. Distinguishing diff ints with the 
            # random incrament.
            x_step = self._step()
            y_step = self._step()

            x = x_step + self.x_points[-1]
            y = y_step + self.y_points[-1]

            if x and y == 0:
                continue

            self.x_points.append(x)
            self.y_points.append(y)

    def _step(self):
        """Used as a helper to consolidate the cosde in run_walk to make it more readible"""
        direction = choice([1, -1])
        distance = choice(list((range(0,5))))
        step = direction * distance

        return step