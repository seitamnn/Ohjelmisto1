# Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
# Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman,
# hakea jo syötetyn lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee
# uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
# Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
# Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy. Käyttäjä saa valita uuden toiminnon
# miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman
# yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK.
# Löydät koodeja helposti selaimen avulla.)
lentoasemat = {}

def lisaa_lentoasema():
    print("Lisätään uusi lentoasema...")
    icao_koodi = input("Syötä lentoaseman ICAO-koodi: ")
    nimi = input("Syötä lentoaseman nimi: ")
    lentoasemat[icao_koodi] = nimi
    print(f"Lentoasema {nimi} lisätty ICAO-koodilla {icao_koodi}.")

def hae_lentoasema():
    icao_koodi = input("Syötä lentoaseman ICAO-koodi, niin haetaan se: ")
    if icao_koodi in lentoasemat:
        print(f"Lentoasema koodilla1 {icao_koodi} on {lentoasemat[icao_koodi]}.")
    else:
        print(f"Lentoasemaa {icao_koodi} ei löytynyt. Aloitetaan alusta.")

while True:
    print("1. Lisää uusi lentoasema")
    print("2. Hae jo olemassa olevan lentoaseman tiedot")
    print("3. Lopeta")

    valinta = input("Valitse toiminto (1/2/3): ")

    if valinta == '1':
        lisaa_lentoasema()
    elif valinta == '2':
        hae_lentoasema()
    elif valinta == '3':
        print("Vai ei lentsikat kiinnosta, höh. Lopetataan sitten.")
        break
    else:
        print("Tuo ei ollut vastausvaihtoehto!!")
        continue