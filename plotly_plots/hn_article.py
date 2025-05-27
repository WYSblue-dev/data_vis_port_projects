import requests
import json
from datetime import datetime as dt
import plotly.express as px


url = 'https://hacker-news.firebaseio.com/v0/item/31353677.json'

r = requests.get(url)
print(f"Status Code {r.status_code}")

response_dict = r.json()
print(response_dict.keys())
response_str = json.dumps(response_dict, indent=4)

print(response_str)
artical_time = dt.fromtimestamp(response_dict['time'])
print(artical_time)
