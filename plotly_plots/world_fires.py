from pathlib import Path

import plotly.express as px
import pandas

path = Path('data_files/eq_data/world_fires_7_day.csv')
df = pandas.read_csv(path, encoding='utf-8')
fig = px.scatter_geo(df, df['latitude'], df['longitude'],
                      color=df['brightness'], color_continuous_scale='hot',
                      labels={'color':'Brightness'},
                      title='WORLD FIRES 1-DAY',
                      )
fig.show()
new_path = Path('/Users/wjerriii/Desktop/plotly_images/fire_globe.html')
fig.write_html(new_path)