# Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
# Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä
# vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina.
# Perehdy rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen,
# jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key).
# Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.
import requests
import json

hakusana = input("Give a city name: ")
api = 'apikey place'
paikkakunta = f'https://api.openweathermap.org/data/2.5/weather?q={hakusana}&appid={api}'
vastaus = requests.get(paikkakunta).json()
print(json.dumps(vastaus, indent=2))
print(f'Weather in {hakusana} is {vastaus["weather"][0]['description']}')
kelvin = vastaus["main"]["temp"]
kelvin = kelvin - 273.15
print(f'Temperature is {kelvin} Celsius')