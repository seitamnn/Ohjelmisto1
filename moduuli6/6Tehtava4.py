# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja
# tulostat sen palauttaman summan.
def summa():
    summattuna = sum(lista_numeroita)
    return summattuna

lista_numeroita = [1,2,3,4,5,6,7,8,9,10]
print("Tässä meillä on lista kokonaislukuja: ", lista_numeroita)
print("Luvut yhteenlaskettuna: ", summa())