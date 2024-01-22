#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes
# käyttäjä antaa negatiivisen tuumamäärän. Sen jälkeen ohjelma lopettaa toimintansa.
# 1 tuuma = 2,54 cm

while True:
    tuuma = float(input("Anna pituus tuumina: "))
    if tuuma < 0:
        print("Annettu numero on negatiivinen. Kokeile aloittaa uudestaan.")
        break
    sentti = tuuma * 2.54
    print(f"{tuuma} tuumaa on {sentti} cm.")
