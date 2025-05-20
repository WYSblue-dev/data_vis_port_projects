from pathlib import Path
import json

import plotly.express as px

path = Path('data_files/eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text(encoding='utf-8')

# this simply assings our json dat to python variable. Essesntially giving us
# dictionary
all_eq_data = json.loads(contents)

all_eq_data = all_eq_data['features']

mags, lats, longs = [], [], []

for eq_data in all_eq_data:
    mag = eq_data['properties']['mag']
    long = eq_data['geometry']['coordinates'][0]
    lat = eq_data['geometry']['coordinates'][1]

    mags.append(mag)
    lats.append(lat)
    longs.append(long)

# this line reforms our data to make it more readable.
readable_contents = json.dumps(all_eq_data, indent=4)

title = 'Global Earthquakes'
fig = px.scatter_geo(lat=lats, lon=longs, size=mags,
                     title=title, color=mags,
                     color_continuous_scale='viridis',
                    #  need to look at why we pas this the wa ywe dp i know its
                    # pandas related of course but a review of why strs etc.
                     labels={'color':'Magnitude'},
                    #  how CAN WE MAKE THE size of the tick labels here bigger?
                    # what about changing the color of the labels as well?\
                    # what about the diffrent colors?
                     projection='natural earth',
                     
                    )
fig.show()

plot_path = Path('/Users/wjerriii/Desktop/all_plots/eq_exploring_data.html')
fig.write_html(plot_path)
# before we write_text be sure to establish a new path obj to write to. Keeps
# og file preserved.
path = Path('data_files/eq_data/readable_eq_all_data.json')
path.write_text(readable_contents)

# read in json data wit hthe json loads function
# we the take the variable and assign it to the dumps so we can write that data
# back but before we do we make it to where the data is formatted more
# consisly with the indet=4 argument we pass to the write_text(method)
