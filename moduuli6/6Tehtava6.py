# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä
# sekä pizzan hinnan euroina. Funktio laskee ja palauttaa pizzan yksikköhinnan euroina
# per neliömetri. Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat
# sekä ilmoittaa, kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi
# yksikköhinta). Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

def laske_hinta(halkaisija, hinta):
    pinta_ala = 0.25 * 3.14159 * (halkaisija ** 2)
    yksikkohinta = hinta / pinta_ala
    return yksikkohinta

halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija: "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta: "))
halkaisija2 = float(input("Anna toisen pizzan halkaisija: "))
hinta2 = float(input("Anna toisen pizzan hinta: "))

yksikkohinta1 = laske_hinta(halkaisija1,hinta1)
yksikkohinta2 = laske_hinta(halkaisija2,hinta2)

if yksikkohinta1 < yksikkohinta2:
    print("Eka pizza antaa paremman vastineen rahalle.")
elif yksikkohinta2 < yksikkohinta1:
    print("Toka pizza antaa paremman vastineen rahalle.")
else:
    print("Molemmat pizzat ovat yhtä kalliita neliömetriä kohden.")