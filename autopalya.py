birsagok = [0] * 24

print("Írd be az adatokat, üres sorig: ")
while True:
    sor = input()
    if sor == "":
        break
    try:
        idopont_sebesseg = sor.split()
        ora_perc = idopont_sebesseg[0].split(":")
        if len(idopont_sebesseg) != 2 or len(ora_perc) != 2:
            raise ValueError()
        ora = int(ora_perc[0])
        perc = int(ora_perc[1])
        sebesseg = int(idopont_sebesseg[1])
    except:
        print("Hibás bemenet:", sor)
        continue
    if sebesseg >= 180:
        birsagok[ora] += 100000
    elif sebesseg >= 140:
        birsagok[ora] += 30000
    else:
        pass

for ora in range(0, 24):
    print(f"{ora:02}:00-{ora:02}:59, {birsagok[ora]} Ft")
