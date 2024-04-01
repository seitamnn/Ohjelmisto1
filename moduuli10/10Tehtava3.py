# Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys,
# joka käskee kaikki hissit pohjakerrokseen.
# Jatka pääohjelmaa siten, että talossasi tulee palohälytys.

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

    def kerros_ylos(self):
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

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissien_lkm = hissien_lkm
        self.hissit = [Hissi(alin_kerros, ylin_kerros, alin_kerros) for _ in range(hissien_lkm)]

    def aja_hissiä(self, hissin_numero, kohdekerros):
        if 0 <= hissin_numero < self.hissien_lkm: #jos hissin nro on min. sama tai isompi kuin 0 ja max. hissien lkm
            self.hissit[hissin_numero].siirry_kerrokseen(kohdekerros)
        else:
            print(f"Hissiä numerolla {hissin_numero} ei ole talossa.")

    def palohalytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin_kerros)

talo = Talo(1, 11, 4)  # Luodaan talo, jossa on kaksi hissiä
print(f'Talossa on {talo.ylin_kerros} kerrosta. Hissien lukumäärä on {len(talo.hissit)}')
talo.aja_hissiä(0, 6)
talo.aja_hissiä(1, 8)

for i, hissi in enumerate(talo.hissit):
    print(f"Hissi {i + 1} on nyt kerroksessa {hissi.kerros_nyt}.")

talo.palohalytys()

for i, hissi in enumerate(talo.hissit):
    print(f"Hissi {i + 1} on nyt kerroksessa {hissi.kerros_nyt}.")