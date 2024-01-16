#Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.
sade = float(input("Anna ympyrän säde: "))
pii = 3.14159265358979323846
pintaala = (pii * sade ** 2)
print("Ympyrän pinta-ala on : " + str(pintaala))