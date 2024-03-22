# Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron.
# Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa.
# Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5),
# metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa,
# että hissi päätyy viidenteen kerrokseen. Viimeksi mainitut metodit ajavat hissiä
# yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on.
# Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi
# kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.

class Hissi:
    def __init__(self, alin_kerros, ylin_kerros, kerros_nyt):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros_nyt = kerros_nyt

    def siirry_kerrokseen(self, kerros):
        self.kerros_nyt = kerros
        if kerros < self.alin_kerros:
            print("Olet nyt alimmassa kerroksessa. Ei päästä enää alöspäin.")
            self.kerros_nyt = self.alin_kerros
            print(f'Olet nyt kerroksessa {self.kerros_nyt}')
            self.kerros_nyt = self.alin_kerros
        if kerros > self.ylin_kerros:
            print("Olet nyt ylimmassa kerroksessa. Ei päästä enää ylöspäin.")
            self.kerros_nyt = self.ylin_kerros
            print(f'Olet nyt kerroksessa {self.kerros_nyt}')

    def kerros_ylös(self):
        self.kerros_nyt = self.kerros_nyt + 1
        if self.kerros_nyt > self.ylin_kerros:
            self.kerros_nyt = self.ylin_kerros
            print("Olet nyt ylimmässä kerroksessa. Ei päästä enää ylöspäin.")
            print(f'Olet nyt kerroksessa {self.kerros_nyt}')

    def kerros_alas(self):
        self.kerros_nyt = self.kerros_nyt - 1
        if self.kerros_nyt < self.alin_kerros:
            self.kerros_nyt = self.alin_kerros
            print("Olet nyt alimmassa kerroksessa. Ei päästä enää ylöspäin.")
            print(f'Olet nyt kerroksessa {self.kerros_nyt}')


h = Hissi(1,10,1)
print(f'Alin kerros: {h.alin_kerros},\nYlin kerros: {h.ylin_kerros},\nKerros nyt: {h.kerros_nyt}\n')
h.siirry_kerrokseen(6)
print(f'Alin kerros: {h.alin_kerros},\nYlin kerros: {h.ylin_kerros},\nKerros nyt: {h.kerros_nyt}\n')
h.kerros_alas()
print(f'Alin kerros: {h.alin_kerros},\nYlin kerros: {h.ylin_kerros},\nKerros nyt: {h.kerros_nyt}\n')
h.kerros_ylös()
print(f'Alin kerros: {h.alin_kerros},\nYlin kerros: {h.ylin_kerros},\nKerros nyt: {h.kerros_nyt}\n')