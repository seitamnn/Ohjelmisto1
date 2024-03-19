# Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa
# tuntimäärässä edennyt. Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km.
# Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus_nyt=0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus_nyt = nopeus_nyt
        self.kuljettu_matka = kuljettu_matka

    def kiihdyta(self, nopeus):
        self.nopeus_nyt = self.nopeus_nyt + nopeus
        if self.nopeus_nyt > self.huippunopeus:
            self.nopeus_nyt = self.huippunopeus

    def hatajarrutus(self):
        self.nopeus_nyt = self.nopeus_nyt - 200
        if self.nopeus_nyt < 0:
            self.nopeus_nyt = 0

    def kulje(self, tuntimaara):
        self.kuljettu_matka = self.nopeus_nyt * tuntimaara


auto = Auto("ABC-123", 142)
print(f"Auton rekisteritunnus: {auto.rekisteritunnus} \nAuton huippunopeus: {auto.huippunopeus} km/h \nAuton tämän hetkinen nopeus: {auto.nopeus_nyt} \nAutolla kuljettu matka: {auto.kuljettu_matka}\n")

print("Kiihdytetään 60km/h.")
auto.kiihdyta(60)
print(f"Auton tämän hetkinen nopeus: {auto.nopeus_nyt}")
print("Ajetaan autolla 3 tuntia.")
auto.kulje(3)
print(f"Autolla kuljettu matka: {auto.kuljettu_matka}")
print("Auton hätäjarrutus! -200 km/h.")
auto.hatajarrutus()
print(f"Auton tämän hetkinen nopeus: {auto.nopeus_nyt}")

