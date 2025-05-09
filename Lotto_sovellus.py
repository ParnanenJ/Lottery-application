import random

# Päälottonumeroiden satunnaisluku generaattori
def plgenerator(alku, loppu, numeroita,):
    lottorivi = []
    while len(lottorivi) != numeroita:
        arvottunum = random.randint(alku, loppu)
        if arvottunum in lottorivi:
            continue
        lottorivi.append(arvottunum)
    return sorted(lottorivi)

def llgenerator(alku, loppu, numeroita):
    lisanumerot = []
    while len(lisanumerot) != numeroita:
        arvottunum = random.randint(alku, loppu)
        if arvottunum in lisanumerot:
            continue
        lisanumerot.append(arvottunum)
    return sorted(lisanumerot)

# Lottorivien määrä
def useampipeli(rivienmaara):
    lottorivit = {}
    if lottopeli == 1:
       for i in range(1, rivienmaara + 1):
            lottorivit[f"Rivi {i}"] = plgenerator(1, 40, 7)
    elif lottopeli == 2:
        for i in range(1, rivienmaara + 1):
            lottorivit[f"Rivi {i}"] = plgenerator(1, 48, 6), llgenerator(1, 5, 1)
    elif lottopeli == 3:
        for i in range(1, rivienmaara + 1):
            lottorivit[f"Rivi {i}"] = plgenerator(1, 50, 5), llgenerator(1, 12, 2)
    return lottorivit

# kysytään syötteet
lottopeli = int(input("Tervetuloa lottosovellukseen!\nTässä on lottopelimme:\n 1) Lotto\n 2) Vikinglotto\n 3) Eurojackpot\nValitse lottopeli (1-3): "))
montalottoa = int(input("Montako lottoriviä haluat luoda (1-10): "))

pelitulostus = ""
if lottopeli == 1:
    pelitulostus = "Lotto"
elif lottopeli == 2:
    pelitulostus = "Vikinglotto"
elif lottopeli == 3:
    pelitulostus = "Eurojackot"

# suoritetaan lottorivien teko
if lottopeli > 0 and lottopeli < 4:
    rivit= useampipeli(montalottoa)
    print(f"\n{'=' * 36}")
    print(pelitulostus.center(36))
    print("=" * 36)
    for n, r in rivit.items():
        if lottopeli == 2 or lottopeli == 3:  # Jos kyseessä on VikingLotto tai Eurojackpot
            pl = " ".join(f"{num:02}" for num in r[0])  # Pääpelin numerot
            ll = " ".join(f"{num:02}" for num in r[1])  # Lisänumerot
            print(f"{n}: {pl} | {ll}".center(36))
        else:  # Jos tavallinen Lotto
            pl = " ".join(f"{num:02}" if num >= 10 else f" {num}" for num in r)  # Yksittäiset numerot saavat eteen tyhjän
            print(f"{n}: {pl}".center(36))
    print("=" * 36)
else:
    print("Lottopeliä ei löytynyt :(")

