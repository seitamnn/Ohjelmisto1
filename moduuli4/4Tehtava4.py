# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus,
# Liian pieni arvaus tai Oikein.
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random
luku = random.randint(1, 10)
while True:
    annettu = int(input('Arvaa luku 1-10 väliltä: '))
    if annettu > luku:
        print('Antamasi luku on liian iso. Kokeile uudestaan!')
    elif annettu < luku:
        print('Antamasi luku on liian pieni. Kokeile uudestaan!')
    elif annettu == luku:
        print(f'Oikein vastattu! Oikea vastaus oli {luku}')
        break