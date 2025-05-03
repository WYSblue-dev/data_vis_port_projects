import plotly.express as px

from rw import RandomWalk as RW

# get random walk data
rw = RW()
rw.run_walk()

# will pass x,y of the walk. what else though
fig = px.scatter(rw.x_points, rw.y_points,)
# px.scatter((0,0), color='red')


fig.show()