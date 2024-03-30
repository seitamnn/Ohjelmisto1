# Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
# Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
# Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä.
# Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa.
# Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:
# - Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
#   Tämä tehdään kutsumalla kiihdytä-metodia.
# - Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
# - Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
#   Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.
import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.matka = 0 # alustetaan nollaksi alussa
        self.nopeus = 0

    def kiihdyta(self, muutos):
        uusi_nopeus = self.nopeus + muutos
        if uusi_nopeus < 0:
            self.nopeus = 0 # jos nopeus olisi pienempi kuin nolla, nopeus asetetaan nollaksi
        elif uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus # ei voi olla enemmän kuin huippunopeus
        else:
            self.nopeus = uusi_nopeus

    def kulje(self):
        self.matka += self.nopeus # 1 tunnin ajan

    def tiedot(self):
        return [self.rekisteritunnus, self.huippunopeus, self.nopeus, self.matka] #tulostaa tiedot niin et saan taulukon


def luo_autot():
    autot = []
    for i in range(1, 11):
        rekisteritunnus = f"ABC-{i}" # i = 1-10
        huippunopeus = random.randint(100, 200) # arvotaan 100-200 välillä
        autot.append(Auto(rekisteritunnus, huippunopeus)) # heitetään taulukkoon
    return autot # palauttaa taulukon


def tulosta_tiedot(autot):
    print("Rekisteritunnus | Huippunopeus (km/h) | Nopeus (km/h) | Matka (km)")
    print("-" * 60) # viiva 60 kertaa
    for auto in autot:
        tiedot = auto.tiedot() #tiedot palauttaa
        print(f"{tiedot[0]:<15} | {tiedot[1]:<20} | {tiedot[2]:<13} | {tiedot[3]}") # numerot tyhjiä merkkejä jotta viivat tulee samalle kohalle ylemmän print-kohdan kanssa

def kilpailu():
    autot = luo_autot()
    print("Ennen kisaa: ")
    tulosta_tiedot(autot) # miltä taulukko näyttää ennen kisaa
    while True:
        for auto in autot:
            muutos = random.randint(-10, 15)
            auto.kiihdyta(muutos)
            auto.kulje()
        voittaja = max(autot, key=lambda x: x.matka) # määritetään listan alkioista se, jolla suurin arvo matka kohdassa
        if voittaja.matka >= 10000: #voittaja on kulkenu 10000km
            break
    print("\nKisan jälkeen: ")
    tulosta_tiedot(autot)

kilpailu()