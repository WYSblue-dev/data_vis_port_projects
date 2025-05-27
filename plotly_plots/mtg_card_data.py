from pathlib import Path
import requests
import json

url = 'https://api.magicthegathering.io/v1/cards?language=English'

headers = {"Accept": "application/json"}

r = requests.get(url, headers=headers)

mtg_data = r.json()
cards_data = json.dumps(mtg_data, indent=4)


path = Path('data_files/json_data/mtg_json_cards.json')

path.write_text(cards_data)

cards = mtg_data['cards']

card_names = []
for card in cards:
    card_names.append(card['name'])

print(len(card_names))