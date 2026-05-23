import os
import requests
from dotenv import load_dotenv

load_dotenv()

scryfall_api_url = os.getenv('SCRYFALL_API_URL')

def search_card(card_name):
    params = {"q": f"name:{card_name}"}
    response = requests.get(scryfall_api_url, params=params)
    data = response.json()
    return data['data'][0] if data.get('data') else None

def get_card_colors(card_name):
    card = search_card(card_name)
    if card:
        return{
            'name': card['name'],
            'mana_cost': card.get('mana_cost',''),
            'colors': card.get('colors', [])
        }
    return None