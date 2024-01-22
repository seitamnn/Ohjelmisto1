# Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja
# hemoglobiiniarvon (g/l). Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.
# Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
# Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

sukupuoli = str(input("Mikä on biologinen sukupuolesi? Vastaa muodossa N tai M: "))
hemo = float(input("Mikä on hemoglobiinisi (g/l)? "))
if sukupuoli == 'N':
    if hemo < 117:
        print("Hemoblobiinisi on alhainen.")
    elif hemo > 175:
        print("Hemoglobiiisi on korkea.")
    else:
        print("Hemoglobiinisi on normaali.")
elif sukupuoli == 'M':
    if hemo < 134:
        print("Hemoblobiinisi on alhainen.")
    elif hemo > 195:
        print("Hemoglobiiisi on korkea.")
    else:
        print("Hemoglobiinisi on normaali.")
else:
    print("Antamasi tieto on virheellinen. Kokeile uudestaan.")