# Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa kyseisessä maassa olevien
# lentokenttien lukumäärät tyypeittäin. Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, että
# pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.

import mysql.connector

def lentokenttien_lkm(maakoodi):
    sql = f"SELECT COUNT(*), type FROM airport where iso_country='{maakoodi}' group by type"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    print(f"Maakoodilla {maakoodi} löytyi")
    for rivi in tulos:
        print(f"{rivi[0]} kpl {rivi[1]}")
    return

yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='root',
    autocommit=True
)

maakoodi = input("Anna maakoodi (esim. FI): ")
lentokenttien_lkm(maakoodi)