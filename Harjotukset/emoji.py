ika = int(input("Anna ikä: "))
if ika >= 1 and ika < 7:
    print("Olet pikkulapsi")
elif ika>=7 and ika < 18:
    print("Olet koululainen")
elif ika>=18 and ika < 70:
    print("Olet työiässä")
else:
    print("Olet eläkeiässä")