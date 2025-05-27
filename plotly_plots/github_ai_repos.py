import requests
import json
from pathlib import Path

# itemgetter most beneficial with something like the sorted functon to sort
# the data based off of a certain key ie. 
# sorted_dict = sorted(data_to_sort, key=itemgetter('key_name'), reverse=True)

# Don't forget we can get a value of a list with list.index('key')
# in a for loop that adds flexability.
from operator import itemgetter

import plotly.express as px

url = 'https://api.github.com/search/repositories'
# this querry would look for repos with the languages having these strs?
url += '?q=topic:ai+sort:stars+stars:>1000'

# setup the headers per the docs to specify what api version to use and what fmt
headers = {'Accept':'application/vnd.github.v3+json'}

# r stand for response. Use the request lib with get to get data
r = requests.get(url, headers=headers)

# convert json to python to access in script
response_dict = r.json()

# format the data and write to a particular path
formatted_dict = json.dumps(response_dict, indent=4)
path = Path('data_files/json_data/ai_related_repos_gh.json')

# we create a ;list of the repos in particular to avoid deep nesting
response_dicts = [repo for repo in response_dict['items']]

# empty liat to store desired data
repo_names, star_gazers, repo_links, hover_texts = [], [], [], []
# we have to use enumerate for access to the element at aspecific index in list
# when this loops it's touching on every dictionasry of the list.
for index, repo_dict in enumerate(response_dicts):
    # pull value of the partcular indexed repo
    repo_name = repo_dict['name']
    repo_names.append(repo_name)

    # plotly let us modify the text elements using html on the html overlay 
    repo_https_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_https_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    hover_name = repo_name
    hover_descrip = repo_dict['description']
    # plotly let us modify the text elements using html on the html overlay 
    hover_text = f"{hover_name}<br />{hover_descrip}"
    hover_texts.append(hover_text)

    # we do want this value and this better shows what's hapening here
    stars = response_dicts[index]['stargazers_count']
    star_gazers.append(stars)


labels = {'x':'Repos',
          'y':'Star Count',
          }

title = 'AI repos soprted by their star count.'.upper()
fig = px.bar(data_frame=(repo_links, star_gazers),
             x=repo_links,
             y=star_gazers,
             labels=labels,
             title=title,
             color=star_gazers,
             color_continuous_scale='matter',
             hover_name=hover_texts,
             )

fig.update_layout(title_font_color='orange',
                  title_font_size=30,
                  xaxis_title_font_color='purple',
                  xaxis_title_font_size=22,
                  yaxis_title_font_color='red',
                  yaxis_title_font_size=24,
                  )

fig.update_coloraxes(colorbar_title='star freq.'.upper(),
                     colorbar_title_font_color='red',
                     colorbar_title_font_size=26,
                     )
if __name__ == '__main__':
    fig.show()