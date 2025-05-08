import random

# satunnaisluku generaattori
def generator(alku, loppu, numeroita,):
    lottorivi = []
    while len(lottorivi) != numeroita:
        arvottunum = random.randint(alku, loppu)
        if arvottunum in lottorivi:
            continue
        lottorivi.append(arvottunum)
    return sorted(lottorivi)

# Lottorivien määrä
def useampipeli(rivienmaara):
    lottorivit = {}
    if lottopeli == 1:
       for i in range(1, rivienmaara + 1):
            lottorivit[f"Rivi {i}"] = generator(1, 40, 7)
    elif lottopeli == 2:
        for i in range(1, rivienmaara + 1):
            lottorivit[f"Rivi {i}"] = generator(1, 48, 6)
    elif lottopeli == 3:
        for i in range(1, rivienmaara + 1):
            lottorivit[f"Rivi {i}"] = generator(1, 50, 5)
    return lottorivit

# kysytään syötteet
lottopeli = int(input("Tervetuloa lottosovellukseen!\nTässä on lottopelimme:\n 1) Lotto\n 2) Vikinglotto\n 3) Eurojackpot\nValitse lottopeli (1-3): "))
montalottoa = int(input("Montako lottoriviä haluat luoda (1-10): "))

# suoritetaan lottorivien teko
if lottopeli > 0 and lottopeli < 4:
    rivit= useampipeli(montalottoa)
    print("\nLottorivisi:")
    print("-------------------------")
    for n, r in rivit.items():
        print(f"{n}: {r}")
else:
    print("Lottopeliä ei löytynyt :(")

