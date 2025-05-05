import plotly.express as px

bjj_data = {
    'catagory':['arbar', 'kimura', 'straight ankle lock', 'heel hook', 'doug choke'],
    'values':[10,20,34,25,12],
}

title_moves = []
for sub in bjj_data['catagory']:
    sub = sub.title()
    title_moves.append(sub)

bjj_data['catagory'] = title_moves

title = 'Frequency of submissions in bjj'.upper()
labels = {'catagory':'Submissions', 'values':'Frequency'}

fig = px.area(bjj_data, x='catagory', y='values', labels=labels, title=title, color='catagory', 
             color_discrete_map={'arbar':'red', 'kimura':'green',
                                  'straight ankle lock':'blue', 'heel hook':'purple',
                                    'doug choke':'black'})

fig.update_layout(
    title_font=dict(color='orange'),
    xaxis_title_font=dict(color='lime'),
    yaxis_title_font=dict(color='lime'),
    xaxis_tickfont=dict(color='black'),
    yaxis_tickfont=dict(color='red'),
)

fig.update_traces()

fig.show()