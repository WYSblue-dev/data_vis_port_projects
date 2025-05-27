import pandas
import plotly.express as px

df = px.data.stocks()

title = "APPLE Vs. GOOGLE"
labels = {'x':'Date', 'y':'Price', 'variable':'Stocks'}
fig = px.line(df, x='date',
              y=['GOOG','AAPL'],
              labels=labels,
              title=title,
              color_discrete_map={'GOOG':'limegreen', 'AAPL':'skyblue'},
            # First time we saw the markers used. Highlights the points.
              markers=True,
              )

fig.update_layout(xaxis_title='Date',
                  yaxis_title='Price',
                  xaxis_title_font_size=30,
                  yaxis_title_font_size=30,
                  xaxis_title_font_color='brown',
                  yaxis_title_font_color='brown',
                  title_font_size=34,
                  title_font_color='red',
                  legend_title_font_size=20,
                  legend_title_font_color='red',
                  )

# notice this is where we customize the markers the we set true in the line plot
# update_traces is specific to the plots themselves hence customizing markers
# here
fig.update_traces(marker_opacity=.6,
                  marker_color='red',
                  )

fig.show()
