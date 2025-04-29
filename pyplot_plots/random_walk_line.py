import matplotlib.pyplot as plt

from pyplot_plots.random_walk import RandomWalk as RW
while True:   
    rw = RW(num_points=5_000)
    rw.run_walk()

    plt.style.use('seaborn-v0_8')

    # could pass the dpi argument here if want for the display res if we know it
    fig, ax = plt.subplots(figsize=(16, 9))

    num_points = range(rw.num_points)
    # edge colors is new here does exactly what is says
    # also it's worth noting the the rang function here passes
    # as accessing the x,y vals via using indexing presumablly through the c= kw call
    ax.plot(rw.x_val, rw.y_val, linewidth=2)

    ax.get_yaxis().set_visible(False)
    ax.get_xaxis().set_visible(False)

    # ax.set_title("Random Walk 5000", fontsize=24)

    # ax.set_xlabel("x-axis".upper(), fontsize=14)
    # ax.set_ylabel("y-axis".upper(), fontsize=14)

    ax.set_aspect('equal')

    plt.tight_layout()

    plt.show()
    keep_running = input("Run again(y/n)?: ")
    keep_running = keep_running.lower()
    if keep_running == 'n':
        break