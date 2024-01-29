# Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
# (käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
# Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä
# kuin ne syötettiin. käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta
# niiden läpikäymiseen.
x = 0
kaupungit = []
for i in range(5):
    annettu = input("Anna kaupunki: ")
    kaupungit.append(annettu)
    i = i + 1
print("Kaupungit samassa järjestyksessä, jossa ne annoit: ")
for x in range(5):
    print(kaupungit[x])
    x = x + 1