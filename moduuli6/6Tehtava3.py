# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain
# nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän.
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
# Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka,
# kunnes käyttäjä syöttää negatiivisen gallonamäärän. Yksi gallona on 3,785 litraa.

def gallonat_litroiksi():
    litrat = gallona * 3.785
    litrat_pyoristettyna_2desimaaliin = round(litrat,2)
    return litrat_pyoristettyna_2desimaaliin

while True:
    gallona = float(input("Anna bensiinin määrä gallonoina: "))
    if gallona < 0:
        print("Ohjelma lopetetaan, koska annoit negatiivisen luvun.")
        break
    print("Bensiinin määrä on tällöin litroina ", gallonat_litroiksi(), "litraa")