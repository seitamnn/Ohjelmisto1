# Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan
# tahkojen yhteismäärän. Muokatun funktion avulla voit heitellä esimerkiksi
# 21-tahkoista roolipelinoppaa. Edellisestä tehtävästä poiketen nopan heittelyä
# jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
# joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

def heitto():
    return random.randint(1,heitot)

heitot = int(input("Anna heitettävän nopan isoin mahdollinen silmäluku: "))
print(f"Heitetään noppaa niin kauan, että saadaan silmäluvuksi {heitot}.")
while True:
    # heitot = 0
    silmaluku = heitto()

    if silmaluku == heitot:
        print(f"Jee sait silmäluvuksi {heitot}! Nyt voidaan lopettaa.")
        break
    else:
        print(f"Silmäluvuksi tuli {silmaluku}. Yritetään vielä...")
        heitto()