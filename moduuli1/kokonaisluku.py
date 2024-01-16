# Kirjoita ohjelma, joka kysyy kolme kokonaislukua.
# Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.

luku1 = int(input("Anna ensimmäinen kokonaisluku: "))
luku2 = int(input("Anna toinen kokonaisluku: "))
luku3 = int(input("Anna kolmas kokonaisluku: "))
summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = (luku1 + luku2 + luku3)/3
print("Antamiesi lukujen summa on: " + str(summa))
print("Antamiesi lukujen tulo on: " + str(tulo))
print("Antamiesi lukujen keskiarvo on: " + str(keskiarvo))