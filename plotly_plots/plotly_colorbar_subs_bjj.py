from pathlib import Path
from datetime import datetime as dt

import plotly.express as px

current_time = dt.now()



# create a pandas like data frame
bjj_data = {
    'catagory':['arbar', 'kimura', 'straight ankle lock', 'heel hook', 'doug choke'],
    'values':[10,20,34,25,12],
}

# capitalize moves
title_moves = []
for sub in bjj_data['catagory']:
    sub = sub.title()
    title_moves.append(sub)

# renames the cata keys with the aray of cap title of moves
bjj_data['catagory'] = title_moves

# sets the title of the plot with upper function
title = 'Frequency of submissions in bjj'.upper()
# assigns diffrent names for the figure ti display diffrent axes labels
labels = {'catagory':'Submissions', 'values':'Frequency'}

# simple aera plot with arguments passed needed and apperence based.
fig = px.area(bjj_data,
              x='catagory',
              y='values',
              labels=labels,
              title=title,
              color='catagory', 
              color_discrete_map={
              'arbar':'red', 'kimura':'green',
              'straight ankle lock':'blue', 'heel hook':'purple',
              'doug choke':'black'})

fig.update_layout(
    title_font=dict(color='orange'),
    xaxis_title_font=dict(color='lime'),
    yaxis_title_font=dict(color='lime'),
    xaxis_tickfont=dict(color='black'),
    yaxis_tickfont=dict(color='red'),
)

# neeed to look into labeling the ledgend better. Title and color along with the
# positiong of the possibale colors.

# neeed to look into what we can do with this further.
fig.update_traces()

fig.show()

path = Path(f'/Users/wjerriii/Desktop/data_vis/plotly_images/{input("Input file name: ")}.html')

fig.write_html(path)