# Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
# Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen
# samalla käyttäjälle, montako senttiä alimmasta sallitusta pyyntimitasta puuttuu.
# Kuha on alamittainen, jos sen pituus on alle 37 cm.

kuhapituus = float(input("Anna kalan pituus senttimetreinä: "))

if kuhapituus < 37:
    puuttuu = 37 - kuhapituus
    print(f"Kuha on liian pieni, laske se veteenkasvamaan! Pituutta tarvitaan vielä {puuttuu} cm.")
else:
    print(f"Kuha on tarpeeksi iso!")