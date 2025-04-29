import matplotlib.pyplot as plt

from pyplot_plots.random_walk import RandomWalk as RW

# run the loop until based by in put
while True:
    # creates instce to get random point values assigned internal of class
    rw_data = RW()
    # method to generate the random points for x and y
    # points will now be contained in the atts of the class obj
    rw_data.run_walk()


    # set the style of our back ground
    plt.style.use('seaborn-v0_8')

    # sets up figure and axes objs as well as sets the screen size.
    fig, ax = plt.subplots(figsize=(16,9))

    # we need to plot our data accordingly
    # need to pass a range of numbers so cmapcan color our points in that order
    num_points = range(rw_data.num_points)
    # edgecolor=None removes black outline making the points more appealing
    ax.scatter(rw_data.x_val, rw_data.y_val, edgecolors=None, c=num_points, cmap=plt.cm.Blues)

    # set the title of our plot
    ax.set_title("Random Walk", fontsize=24, color='grey')

    ax.set_xlabel('X - axis'.upper(), fontsize=14)
    ax.set_ylabel('y - axis'.upper(), fontsize=14)

    # set the graph to visually be appealing with auto scaleing the axes
    ax.set_aspect('equal')

    # runs the matplotlib viewer to see plot
    plt.show()

    # sets input question
    rerun = input("Run again?(y/n): ")
    # corrects for errors
    rerun = rerun.lower()
    # conditional test for str char
    if rerun == 'n':
        # stops while loop with a break
        break