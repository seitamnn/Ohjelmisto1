# Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
#     kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
#     nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.
# !En tiedä oliko sallittua käyttää looppeja, mutta voin tehdä uudestaan jos ei kelpaa!
import random

print("Kolmenumeroinen satunnaisesti generoitu koodi (0-9): ")
for _ in range(3):
    kolme = random.randint(0, 9)
    print(kolme)

print("Nelinumeroinen satunnaisesti generoitu koodi (1-6): ")
for _ in range(4):
    nelja = random.randint(1, 6)
    print(nelja)