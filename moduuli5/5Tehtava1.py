# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
# Käytä for-toistorakennetta.
import random

lukumaara = int(input("Anna arpakuutioiden lukumäärä: "))
summa = 0

for i in range(lukumaara):
    nopat = random.randint(1,6)
    summa += nopat

print(f"Arpakuution silmälukujen summa on {summa}.")
