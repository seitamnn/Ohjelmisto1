# Kirjoita parametriton funktio, joka palauttaa paluuarvonaan
# satunnaisen nopan silmäluvun väliltä 1..6. Kirjoita pääohjelma,
# joka heittää noppaa niin kauan kunnes tulee kuutonen.
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.
import random

def heitto():
    return random.randint(1,6)

print("Heitetään noppaa niin kauan, että saadaan silmäluvuksi 6.")
while True:
    heittoja = 0
    silmaluku = heitto()

    if silmaluku == 6:
        print("Jee sait kutosen! Nyt voidaan lopettaa.")
        break
    else:
        print(f"Silmäluvuksi tuli {silmaluku}. Yritetään vielä...")
        heitto()