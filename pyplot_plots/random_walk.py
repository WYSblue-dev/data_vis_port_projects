from random import choice

class RandomWalk:
    """Used to generate data that alligns withe the random walk idea."""

    def __init__(self, num_points=5000):
        """Initializes the atts the class needs wiht the instance when created."""
        # sets default to 5000 unless specified otherwise
        self.num_points = num_points

        self.x_val = [0]
        self.y_val = [0]
    
    def run_walk(self):
        """Used to generate the data itself to stor with our atts."""
        while len(self.y_val) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step and y_step == 0:
                continue

            x = self.x_val[-1] + x_step
            y = self.y_val[-1] + y_step

            self.x_val.append(x)
            self.y_val.append(y)

    def get_step(self):
        """gets the random step int we need for a random walk."""
        direction = [1, -1]
        distance = [0, 1, 2, 3, 4, 5]
        step = choice(direction) * choice(distance)
        return step