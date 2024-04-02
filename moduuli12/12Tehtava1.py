# Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle.
# Käytä seuravalla sivulla esiteltävää rajapintaa: https://api.chucknorris.io/.
# Käyttäjälle on näytettävä pelkkä vitsin teksti.
import requests
# import json

get_quote = "https://api.chucknorris.io/jokes/random"
quote = requests.get(get_quote).json()
#print(json.dumps(quote, indent=2))
print(quote["value"])