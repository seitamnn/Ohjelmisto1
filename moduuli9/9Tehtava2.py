# Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan
# nopeuden muutoksen (km/h). Jos nopeuden muutos on negatiivinen, auto hidastaa.
# Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
# Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
# Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h
# ja lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus.
# Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
# Kuljettua matkaa ei tarvitse vielä päivittää.

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

auto = Auto("ABC-123", 142)
print(f"Auton rekisteritunnus: {auto.rekisteritunnus} \nAuton huippunopeus: {auto.huippunopeus} km/h \nAuton tämän hetkinen nopeus: {auto.nopeus_nyt} \nAutolla kuljettu matka: {auto.kuljettu_matka}")

print("Kiihdytetään 30km/h.")
auto.kiihdyta(30)
print(f"Auton tämän hetkinen nopeus: {auto.nopeus_nyt}")
print("Kiihdytetään 70km/h.")
auto.kiihdyta(70)
print(f"Auton tämän hetkinen nopeus: {auto.nopeus_nyt}")
print("Kiihdytetään 50km/h.")
auto.kiihdyta(50)
print(f"Auton tämän hetkinen nopeus: {auto.nopeus_nyt}")
print("Auton hätäjarrutus! -200 km/h.")
auto.hatajarrutus()
print(f"Auton tämän hetkinen nopeus: {auto.nopeus_nyt}")