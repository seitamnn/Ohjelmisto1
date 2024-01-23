# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

luvut = []
while True:
    annettu = input("Anna luku. Kun haluat lopettaa anna tyhjä vastaus ja järjestän luvut: ")
    if annettu == '':
        print('Noniin, annoit tyhjän vastauksen. Järjestän luvut nyt pienimmästä suurimpaan.')
        break
    luvut.append(annettu)
    print(luvut)
luvut.sort()
print(f"Tässä: {luvut}")