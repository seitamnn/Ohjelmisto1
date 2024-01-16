# Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten
# mittojen mukaan leivisköinä, nauloina ja luoteina.
# Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi
# sekä ilmoittaa tuloksen käyttäjälle.
#    Yksi leiviskä on 20 naulaa.
#    Yksi naula on 32 luotia.
#    Yksi luoti on 13,3 grammaa.


leiviska = float(input("Anna leiviskät: "))
naula = float(input("Anna naulat: "))
luoti = float(input("Anna luodit: "))

leiviskat = leiviska * 20 * 32 * 13.3
naulat = naula * 32 * 13.3
luodit = luoti * 13.3

massa = leiviskat + naulat + luodit
kg = massa / 1000

print("Massa nykymittojen mukaan: " + str(kg) + " kg")

