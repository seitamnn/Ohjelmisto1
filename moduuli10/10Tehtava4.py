# Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun nimi,
# pituus kilometreinä ja osallistuvien autojen lista. Luokassa on alustaja,
# joka saa parametreinaan nimen, kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi.
# Luokassa on seuraavat metodit:
#   tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät
#   toimenpiteet eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.
#   tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
#   kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun
#   kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.
# Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli".
# Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä.
# Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa tunti_kuluu-metodia,
# jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi.
# Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin
# välein sekä kertaalleen sen jälkeen, kun kilpailu on päättynyt.


import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.matka = 0  # alustetaan nollaksi alussa
        self.nopeus = 0

    def kiihdyta(self, muutos):
        uusi_nopeus = self.nopeus + muutos
        if uusi_nopeus < 0:
            self.nopeus = 0  # jos nopeus olisi pienempi kuin nolla, nopeus asetetaan nollaksi
        elif uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus  # ei voi olla enemmän kuin huippunopeus!!
        else:
            self.nopeus = uusi_nopeus

    def kulje(self):
        self.matka += self.nopeus  # 1 tunnin ajan

    def tiedot(self): # tulostaa tiedot niin et saan taulukon
        return [self.rekisteritunnus, self.huippunopeus, self.nopeus,
                self.matka]


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-10, 15)
            auto.kiihdyta(muutos)
            auto.kulje()

    def tulosta_tilanne(self): # taulukon tulostus
        print("Rekisteritunnus | Huippunopeus (km/h) | Nopeus (km/h) | Matka (km)")
        print("-" * 60)  # viiva 60 kertaa
        for auto in self.autot:
            tiedot = auto.tiedot()  # tiedot palauttaa
            print(
                f"{tiedot[0]:<15} | {tiedot[1]:<20} | {tiedot[2]:<13} | {tiedot[3]}")  # numerot tyhjiä merkkejä jotta viivat tulee samalle kohalle ylemmän print-kohdan kanssa

    def kilpailu_ohi(self): # katotaan onko kilpailu käynnis
        for auto in self.autot:
            if auto.matka >= self.pituus: # jos auton kuljettu matka sama tai isompi ku kilpailun pituus
                return True
        return False


def luo_autot():
    autot = []
    for i in range(1, 11):
        rekisteritunnus = f"ABC-{i}"
        huippunopeus = random.randint(100, 200)  # arvotaan 100-200 välillä
        autot.append(Auto(rekisteritunnus, huippunopeus))  # heitetään taulukkoon
    return autot  # palauttaa taulukon


def paaohjelma():
    autot = luo_autot()
    kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

    print("Ready, set, GOOOO!")
    kilpailun_kesto = 0
    while not kilpailu.kilpailu_ohi():
        kilpailu.tunti_kuluu()
        kilpailun_kesto += 1
        if kilpailun_kesto % 10 == 0:  # 10 tunnin välein
            print(f"\nTilanne kilpailussa {kilpailun_kesto} tunnin jälkeen: ")
            kilpailu.tulosta_tilanne()

    print("\nKilpailu päättyi")
    kilpailu.tulosta_tilanne()

paaohjelma()