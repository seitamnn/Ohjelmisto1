# Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
# Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä.
# Laskenta perustuu tietokannasta haettuihin koordinaatteihin.
# Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/.
# Asenna kirjasto valitsemalla View / Tool Windows / Python Packages.
# Kirjoita hakukenttään geopy ja vie asennus loppuun.

from geopy import distance
import mysql.connector

def hae_tiedot(ICAO):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{ICAO}'"
    # print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    return tulos

yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)
eka = hae_tiedot(input("Anna eka ICAO koodi: "))
toka = hae_tiedot(input("Anna toka ICAO koodi: "))

valimatka = distance.geodesic(eka, toka)

print(f"Lentokenttien välinen välimatka on {valimatka}")

#print(eka)
#print(toka)