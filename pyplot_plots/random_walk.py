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
            x_direction = [10, -1]
            x_distance = [0, 1, 2, 3, 4, 5]
            x_val = choice(x_direction) * choice(x_distance)

            y_direction = [1, -1]
            y_distance = [0, 1, 2, 3, 4, 5]
            y_val = choice(y_direction) * choice(y_distance)

            if x_val and y_val == 0:
                continue

            x = self.x_val[-1] + x_val
            y = self.y_val[-1] + y_val

            self.x_val.append(x)
            self.y_val.append(y)
