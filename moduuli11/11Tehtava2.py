# Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
# Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina.
# Polttomoottoriauton ominaisuutena on bensatankin koko litroina.
# Kirjoita aliluokille alustajat. Esimerkiksi sähköauton alustaja saa parametreinaan
# rekisteritunnuksen, huippunopeuden ja akkukapasiteetin.
# Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa.
# Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh)
# ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l).
# Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran ja
# tulosta autojen matkamittarilukemat.

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

class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko

def aja_auto(auto, tuntien_maara):
    for _ in range(tuntien_maara):
        muutos = random.randint(-10, 15)
        auto.kiihdyta(muutos)
        auto.kulje()

def paaohjelma():
    sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
    polttomoottori = Polttomoottoriauto("ACD-123", 165, 32.3)

    sahkoauto.kiihdyta(105)
    polttomoottori.kiihdyta(100) # Asetetaan polttomoottoriautolle nopeus

    aja_auto(sahkoauto, 3)
    aja_auto(polttomoottori, 3)

    print("Sähköauton matkamittarilukema:", sahkoauto.matka, "km")
    print("Polttomoottoriauton matkamittarilukema:", polttomoottori.matka, "km")


paaohjelma()