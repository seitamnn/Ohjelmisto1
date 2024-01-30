# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron,
# jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
# Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten,
# että joulukuu on ensimmäinen talvikuukausi.

kuukaudet = ("tammi", "helmi", "maalis", "huhti", "touko", "kesä", "heinä", "elo", "syys", "loka", "marras", "joulu")
# oisin halunnut tehdä dictionaryna mut tehtävän mukaan monikkona
annettu_numero = int(input("Anna kuukauden numero: "))
kk = kuukaudet[annettu_numero-1]

if kk == "tammi" or kk == "huhti" or kk == "heinä" or kk =="loka":
    mones = "toinen"
elif kk == "helmi" or kk == "touko" or kk == "elo" or kk =="marras":
    mones = "kolmas"
elif kk == "joulu" or kk == "maalis" or kk == "kesä" or kk =="syys":
    mones = "ensimmäinen"

if kk == "joulu" or kk == "tammi" or "helmi":
    vuodenaika = "talvi"
elif kk == "maalis" or kk == "huhti" or "touko":
    vuodenaika = "kevät"
elif kk == "kesä" or kk == "heinä" or "elo":
    vuodenaika = "kesä"
elif kk == "syys" or kk == "loka" or "marras":
    vuodenaika = "syys"

print(f"{kk}kuu on {mones} {vuodenaika}kuukausi")


