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

# suoritetaan lottorivien teko
if lottopeli > 0 and lottopeli < 4:
    rivit= useampipeli(montalottoa)
    print(f"\n{'=' * 35}")
    print("Lottorivisi:")
    print("=" * 35)
    for n, r in rivit.items():
        if lottopeli == 2 or lottopeli == 3:  # Jos kyseessä on tuple (VikingLotto tai Eurojackpot)
            print(f"{n}: ", *r[0], "|", *r[1])
        else:  # Jos kyseessä on tavallinen Lotto
            print(f"{n}: ", *r)
    print("=" * 35)
else:
    print("Lottopeliä ei löytynyt :(")

