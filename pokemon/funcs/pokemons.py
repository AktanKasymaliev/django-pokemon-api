import json

import requests

def request(url: str) -> dict:
    response = requests.get(url)
    return json.loads(response.text)

def get_pokemon(pokemon_name: str) -> dict:
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = request(url)
    name = response["name"]
    height = response["height"]
    ability_one = response["abilities"][0]["ability"]["name"]
    ability_two = response["abilities"][1]["ability"]["name"]
    base_experience = response["base_experience"]
    context = {
        "name": name,
        "height": height,
        "ability_one": ability_one,
        "ability_two": ability_two,
        "base_experince": base_experience
                }
    return context

