import random

# Päälottonumeroiden satunnaisluku generaattori
def plgenerator(alku, loppu, numeroita,):
    lottorivi = []
    while len(lottorivi) != numeroita: # Arvotaan niin monta numeroa kuin parametrille "numeroita" on annettu arvoksi
        arvottunum = random.randint(alku, loppu) # arvotaan numerot annetuiden "alku" ja "loppu" parametrien välistä
        if arvottunum in lottorivi: # Tarkistetaan ettei luku ole jo listassa
            continue
        lottorivi.append(arvottunum) # Lisätään arvottu numero listaan
    return sorted(lottorivi) # Palautetaan lita järjestyksessä pienimmästä suurimpaan

# Lottorivien määrä
def useampipeli(rivienmaara):
    lottorivit = {}
    if lottopeli == 1:
       for i in range(1, rivienmaara + 1):
            lottorivit[f"Rivi {i}"] = plgenerator(1, 40, 7) # Pelataan Lotto rivit ja tallennetaan ne kirjastoon
    elif lottopeli == 2:
        for i in range(1, rivienmaara + 1):
            lottorivit[f"Rivi {i}"] = plgenerator(1, 48, 6), plgenerator(1, 5, 1) # Pelataan Vikinglotto rivit ja tallennetaan ne kirjastoon
    elif lottopeli == 3:
        for i in range(1, rivienmaara + 1):
            lottorivit[f"Rivi {i}"] = plgenerator(1, 50, 5), plgenerator(1, 12, 2) # Pelataan Eurojackpot rivit ja tallennetaan ne kirjastoon
    return lottorivit

# Tuosten tallentaminen tiedostoon nimeltä "Aiemmat_pelit.txt"
def tallennus(tulokset):
    while True:
        paatos = input("Haluatko tallentaa pelirivit tiedostoon?\nKyllä = 'k' ja Ei = 'e': ").upper()
        if paatos == "K":
            with open("Aiemmat_pelit.txt", "a") as tiedosto:
                tiedosto.write(f"{tulokset}\n{'=' * 36}") # Tallennetaan tulokset tiedostoon
            print("Pelirivit tallennettu!")
            break
        elif paatos == "E":
            print("Tietoja ei tallennettu.")
            break
        else:
            print("Syötettä ei tunnistettu.")

print("Tervetuloa lottosovellukseen!")
while True:
    # kysytään syötteet
    try:
        lottopeli = int(input("Tässä on lottopelimme:\n 1) Lotto\n 2) Vikinglotto\n 3) Eurojackpot\nValitse lottopeli (1-3): ")) # Peli
        montalottoa = int(input("Montako lottoriviä haluat luoda (1-10): ")) # Rivien määrä
    except:
        print("Virheellinen syöte.")
        continue

    # Valitaan pelin nimi tulostukseen
    pelitulostus = ""
    if lottopeli == 1:
        pelitulostus = "Lotto"
    elif lottopeli == 2:
        pelitulostus = "Vikinglotto"
    elif lottopeli == 3:
        pelitulostus = "Eurojackot"

    # suoritetaan lottorivien teko
    if lottopeli > 0 and lottopeli < 4:
        tulokset = f"\n{'=' * 36}\n{pelitulostus.center(36)}\n{'=' * 36}" # Alustetaan tellennukseen menevä muuttujan tuloste
        rivit = useampipeli(montalottoa)
        print(f"\n{'=' * 36}")
        print(pelitulostus.center(36)) # Tulostetaan pelin nimi
        print("=" * 36)
        for n, r in rivit.items():
            if lottopeli == 2 or lottopeli == 3:  # Jos kyseessä on VikingLotto tai Eurojackpot
                pl = " ".join(f"{num:02}" if num >= 10 else f" {num}" for num in r[0])  # Pääpelin numerot
                ll = " ".join(f"{num:02}" if num >= 10 else f" {num}" for num in r[1])  # Lisänumerot
                tulokset += f"\n{n}: {pl} | {ll}".center(36)   # Lisätään rivi muuttajaan tallennusta varten
                print(f"{n}: {pl} | {ll}".center(36)) # Tulostetaan rivit
            else:  # Jos tavallinen Lotto
                pl = " ".join(f"{num:02}" if num >= 10 else f" {num}" for num in r)  # Yksittäiset numerot saavat eteen tyhjän
                tulokset += f"\n{n}: {pl}".center(36)   # Lisätään rivi muuttajaan tallennusta varten
                print(f"{n}: {pl}".center(36)) # Tulostetaan rivit
        print("=" * 36)
    else:
        print("Lottopeliä ei löytynyt :(")
        continue

    tallennus(tulokset) # Tallennetaanko rivit?

    # Jatketaanko pelaamista vai lopetetaanko se
    while True:
        try:
            jatko = int(input("\nKiitos pelaamisesta!\n 1) Jatka pelaamista\n 2) Näytä tallennetut rivit\n 3) Lopeta\nValitse (1-3): "))
            if jatko == 1: # Jatko
                print("Jatketaan pelaamista.")
                break
            elif jatko == 2: # Tulostetaan tallennetut pelit
                print("Tallennetut rivit:\n")
                with open("Aiemmat_pelit.txt") as tiedosto:
                    print(tiedosto.read())
            elif jatko == 3: # Lopetus
                break   
            else:
                print("Syötettä ei tunnistettu.")
        except:
            print("Syötettä ei tunnistettu.")

    if jatko == 3: # Lopetetaan sovelluksen suorittaminen
        print("Lopetetaan sovellus!")
        break
