from operator import itemgetter
from pathlib import Path
import json
import requests

# make an api call and check the response
# this url gets a list of the topstories with the numbers
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)

# convert the information to a python dict for each submission
submission_arts = r.json()

# make a list for the numbers corlting to the article
submission_ids = [sub_id for sub_id in submission_arts]

# we need a good way to store formatted json data???????
top_articles = []

# access for the first 30 top stories
# take the urls and then querry through them and format to get clean json.
for id in submission_ids[:30]:
    # check response code wit hthe id
    print(f"id: {id}\tStatus Code - {r.status_code}")
    # status code 200 means next query will work
    url = f'https://hacker-news.firebaseio.com/v0/item/{id}.json'
    # request specific story
    r = requests.get(url)
    # convert to python dictionary
    response_dict = r.json()
    # convert to formatted json for readability
    # how do we add a way for this to be a continual dict in a data container?
    top_articles.append(response_dict)

# this is our first time using itemgetter and it seems extremely beneficial
# can sort based on a particular value associated with a key ie 'score'
top_sorted_arts = sorted(top_articles, key=itemgetter('score'), reverse=True)
# set up path file obj for where we want to save
new_path = Path('data_files/json_data/articles.json')
content = json.dumps(top_sorted_arts, indent=4)
new_path.write_text(content)