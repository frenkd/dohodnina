from dohodnina import splosna_olajsava, letna_dohodnina_lestvica


def izracunaj_dohodnino(bruto_zasluzek,
                        invalid=False,
                        prijavljen_kot_vzdrzevan=True,
                        stroski_prevoza_in_nocitve=0,
                        izpisi=False):

    # =======================
    # Prispevki (za pokojninsko in invalidsko zavarovanje)
    # =======================
    # Študenti:  15.5%
    prispevki = bruto_zasluzek * 0.155

    # =======================
    # Davčne olajšave (letno)
    # =======================
    # 1. Splošna olajšava
    # Upošteva se, če te starši ne prijavijo kot vzdrževanega otroka oz. druzinskega člana
    znesek_splosna_olajsava = splosna_olajsava(
        bruto_zasluzek) if not prijavljen_kot_vzdrzevan else 0

    # 2. Osebne olajsave za 100% invalide
    znesek_olajsava_za_invalide = 17658.84 if invalid else 0

    # 3. Posebna osebna olajšava
    # Za rezidenta, ki se izobražuje in ima status dijaka ali študenta, znaša 3.500,00 eura.
    znesek_posebna_osebna_olajsava = 3500
    # Davčna osnova je zmanjšana za normirane stroške v višini 10 % od doseženega dohodka
    znesek_normirani_stroski = bruto_zasluzek * 0.10
    # Poleg normiranih stroškov lahko dijak ali študent uveljavlja tudi dejanske stroške prevoza in nočitve
    znesek_stroski_prevoza_in_nocitve = stroski_prevoza_in_nocitve
    znesek_dodatna_studentska_olajsava = znesek_normirani_stroski + \
        znesek_stroski_prevoza_in_nocitve

    # 4. Posebna olajšava
    # Predpostavka (v robnem primeru verjetno zmotna),
    # da večina študentov nima vzdrževanih otrok/družinskih članov

    # 4. Olajšava za prostovoljno dodatno pokojninsko zavarovanje
    # Predpostavka (v robnem primeru verjetno zmotna),
    # da večina študentov ne razmišlja o dodatnem pokojninskem zavarovanju
    # (ali pa da bomo dočakali penzijo lol)

    # =======================
    # Poračun
    # =======================
    olajsave = znesek_splosna_olajsava \
        + znesek_olajsava_za_invalide \
        + znesek_posebna_osebna_olajsava \
        + znesek_dodatna_studentska_olajsava \

    # Neto letna davcna osnova
    neto_davcna_osnova = bruto_zasluzek - prispevki - olajsave
    # Omejimo se na pozitivne vsote
    neto_davcna_osnova = max(neto_davcna_osnova, 0)

    # Stopnja dohodnine (letno)
    letna_dohodnina = letna_dohodnina_lestvica(neto_davcna_osnova)

    if izpisi:
        print(f"Bruto letni zaslužek: {bruto_zasluzek:.2f}€")
        print(f"Prispevki: {prispevki:.2f}€")
        print(f"'Neto' letni zaslužek: {(bruto_zasluzek - prispevki):.2f}€")
        print(f"Olajšave skupaj: {olajsave:.2f}€")
        print(f"Neto letna davčna osnova: {neto_davcna_osnova:.2f}€")
        print(f"Letna dohodnina: {letna_dohodnina:.2f}€")
        print(
            f"Dejanski neto letni zaslužek: {(bruto_zasluzek - prispevki - letna_dohodnina):.2f}€")

    return letna_dohodnina


def main():
    print("***| Informativni izracun dohodnine za študenta |***\n")
    bruto_letni_zasluzek = float(input("Vnesite svoj bruto letni zasluzek: "))

    prijavljen_kot_vzdrzevan = bool(
        input("Vas bodo starši prijavili kot vzdrževanega otroka/družinskega člana? (y/N): ").lower() == 'y')

    invalid = input(
        "Ste invalid s 100% telesno okvaro? (y/N): ").lower() == 'y'

    stroski_prevoza_in_nocitve = float(
        input("Uveljavljeni dejanski stroški prevoza in nočitve (eur): "))

    print("\nIzračun:\n")

    izracunaj_dohodnino(
        bruto_zasluzek=bruto_letni_zasluzek,
        prijavljen_kot_vzdrzevan=prijavljen_kot_vzdrzevan,
        invalid=invalid,
        stroski_prevoza_in_nocitve=stroski_prevoza_in_nocitve,
        izpisi=True
    )

if __name__ == "__main__":
    main()
