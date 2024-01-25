# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille
# argumentiksi reverse=True.
jono = []
while True:
    annettu = input("Anna luku. Kun haluat lopettaa paina ENTER: ")
    if annettu == "":
        print("Höh haluut jo lopettaa..... :(")
        suurimmat = sorted(jono, reverse=True)[:5]
        print(f"Antamistasi luvuista 5 suurinta ovat :{suurimmat}")
        break
    else:
        jono.append(int(annettu))