#Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
# Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja
# sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
# ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.
import mysql.connector

def hae_icao_koodi(icao_koodi):
    sql = f"SELECT name, municipality FROM airport where ident='{icao_koodi}'"
    # print(sql)
    kursori = yhteys.cursor() #yhteys juu
    kursori.execute(sql) #suorittaa sql lauseen
    tulos = kursori.fetchall() # tulos pyydetään palvelimelta
    if kursori.rowcount > 0: # käydään läpi halutut rivit jeejee
        for rivi in tulos:
            print(f"{icao_koodi} vastaava lentokenttä on {rivi[0]} ja se sijaitsee paikassa {rivi[1]}")
    return

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='root',
         autocommit=True
         )

icao_koodi = input("Anna lentokentän icao koodi: ")
hae_icao_koodi(icao_koodi)