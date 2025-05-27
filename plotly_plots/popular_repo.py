from pathlib import Path
import json
import requests

import plotly.express as px
import pandas as pd

url = 'https://api.github.com/search/repositories'
url += '?q=language:css+sort:stars+stars:>10000'

headers = {'Accept':'application/vnd.github.v3+json'}

r = requests.get(url, headers=headers)

response_dict = r.json()

# have to write to a file so it exist so then the data frame has access
path = Path('data_files/json_data/github_api_request.json')
# had to import json to convert from python to json data format to then
# be able to write it to a file in pur data folder 
json_data = json.dumps(response_dict, indent=4)
path.write_text(json_data)
# example of maybe using a dataframe instead
df = pd.read_json(path)
# this idea of a dataframe is interesting but to work with it more efficently 
# will take some time for sure. We could use something like df.head() to trouble

response_repos = [repo for repo in response_dict['items']]

repo_star_data, repo_name_link_data, hover_texts = [], [], []

# the response repos var is a list of the repos that are indi dicts
# therfore repo her in enumerate ar the dicts. Enum may be useless here bc
# a simple loop would've sufficed i think
for index, repo in enumerate(response_repos):
    name = repo['name']
    link = repo['html_url']
    name_url = f"<a href='{link}'>{name}</a>"
    # shows the diffrences of how we can get the data here. Using enum repo nice
    stars = response_repos[index]['stargazers_count']

    owner = repo['owner']['login']
    description = repo['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

    repo_star_data.append(stars)
    repo_name_link_data.append(name_url)

title = "Most Popular Github Repos(Stars)"
labels = {'x':'Repo Name', 'y':'Stars', 'color':'Star Count'}

fig = px.bar(x=repo_name_link_data,
             y=repo_star_data,
             title=title,
             labels=labels,
             color=repo_star_data,
             color_continuous_scale='hot',
             hover_name=hover_texts,
             )

fig.update_layout(title_font_size=28,
                  xaxis_title_font_size=22,
                  yaxis_title_font_size=22,
                  )
# interesting that the docs refrence this other method to call but we could've
# elft the coloraxis_colorbar....etc in the update_layout method call
fig.update_coloraxes(colorbar_title_font_size=30,
                  colorbar_showticklabels=True,
                  colorbar_tickfont_size=18,
                  )

# what is this doing and why is it refrenced in the update traces area?
# we can look at the fig object however though and see where the coloraxis 
# resides giving us a clue as to where we should be wroking with this particular
# property to change the appearence

# this is wring chekc the term fig obj printed
# fig.update_traces(marker_colorbar_showticklabels=False)
if __name__ == '__main__':
    fig.show()

# interesting obj call ere to see what's happening with the plot to some degree.
print(fig)