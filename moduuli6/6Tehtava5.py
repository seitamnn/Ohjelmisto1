# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin
# parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat
# sen jälkeen sekä alkuperäisen että karsitun listan.

def poista_parittomat(lista):
    return [luku for luku in lista if luku % 2 == 0]

alkuperainen_lista = [1,2,3,4,5,6,7,8,9,10]
lista_ilman_parittomia = poista_parittomat(alkuperainen_lista)
print("Alkuperäinen lista on tässä: ", alkuperainen_lista)
print("Lista ilman parittomia lukuja on tässä: ", lista_ilman_parittomia)
