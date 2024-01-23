# Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
# (Oikea käyttäjätunnus on python ja salasana rules).

kayttaja = 'python'
salasana = 'rules'
kerta = 5
while True:
    annettu_kayttaja = input('Anna käyttäjätunnus: ')
    annettu_salasana = input('Anna salasana: ')
    kerta = kerta-1
    if annettu_kayttaja == kayttaja and annettu_salasana == salasana and kerta >=1:
        print('Tervetuloa!')
        break
    else:
        if kerta <= 0:
            print('Olet yrittänyt kirjautua 5 kertaa. Yritä hetken päästä uudestaan.')
            break
        print(f'Pääsy evätty. Voit yrittää vielä {kerta} kertaa uudestaan.')