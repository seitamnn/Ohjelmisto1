# Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden.
# Ohjelma tulostaa suorakulmion piirin ja pinta-alan.
# Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.

kanta = float(input("Anna suorakulmion kanta: "))
korkeus = float(input("Anna suorakulmion korkeus: "))
piiri = kanta + korkeus + kanta + korkeus
pintaala = kanta * korkeus
print("Suorakulmion piiri on: " + str(piiri))
print("Suorakulmion pinta-ala on: " + str(pintaala))