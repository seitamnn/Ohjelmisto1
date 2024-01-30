# Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka,
# kunnes käyttäjä syöttää tyhjän merkkijonon. Kunkin nimen syöttämisen jälkeen
# ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan,
# syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet
# yksi kerrallaan allekkain mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta
# nimien tallentamiseen.
nimet = set()
while True:
    nimi = input("Anna nimi. Kun haluat lopettaa, paina vain ENTER: ")
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
    if nimi == "":
        print("Hööööh haluut jo lopettaa")
        break
    nimet.add(nimi)
print("Antamasi nimet mielivaltaisessa järjestyksessä: ")
for nimi in nimet:
    print(nimi)