# used to see what graphs are made when simply
from datetime import datetime as dt
from rw import RandomWalk as RW

import plotly.express as px


time = dt.now()

# get random walk data
rw = RW()
rw.run_walk()

title = str(time)
labels = {'x':'x_axis', 'y':'virt_dir'}

fig = px.line(x=rw.x_points, y=rw.y_points, labels=labels, title=title)

fig.update_traces(line_color='red')

fig.update_layout(
    xaxis_title_font=dict(color='red'),
    yaxis_title_font=dict(color='blue'),
    xaxis_tickfont=dict(color='orange'),
    yaxis_tickfont=dict(color='orange'),
)

fig.show()