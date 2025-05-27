from pathlib import Path
import json
from datetime import datetime as dt

import plotly.express as px

path = Path('data_files/eq_data/eq_data_30_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
json_data = json.loads(contents)

# get the eq specific data
all_eq_data = [eq_data for eq_data in json_data['features']]

mags = [eq['properties']['mag'] for eq in all_eq_data]
lats = [eq['geometry']['coordinates'][1] for eq in all_eq_data]
logs = [eq['geometry']['coordinates'][0] for eq in all_eq_data]
times = [dt.fromtimestamp((eq['properties']['time']/1000)).date() for eq in all_eq_data]
locos = [eq['properties']['place'] for eq in all_eq_data]
eq_titles = [eq['properties']['title'] for eq in all_eq_data]

title = f'{json_data['metadata']['title']}'.upper()

fig = px.scatter_geo(lat=lats, lon=logs,
                     size=mags,
                     color=mags,
                     hover_name=eq_titles,
                     hover_data={'Date':times},
                     color_continuous_scale='hot',
                     title=title,
                     labels={'color':'magnitude'},
                     projection='natural earth'
                     )
# if we wanted to dd more ciustomiztion refer docs. laypout and traces mybe axes
fig.update_layout(title_font_color='red')

fig.show()

new_path = Path('data_files/eq_data/readable_eq_30.json')

fig.write_html(new_path)
