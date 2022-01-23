from dohodnina import splosna_olajsava, letna_dohodnina_lestvica, olajsava_vzdrzevani_otroci, olajsava_vzdrzevani_druzinski_clani


def izracunaj_dohodnino(bruto_zasluzek,
                        invalid=False,
                        stevilo_vzdrzevanih_otrok=0,
                        stevilo_vzdrzevanih_druzinskih_clanov=0,
                        stevilo_vzdrzevanih_mesecev=12,
                        premija_dod_pok_zav=0,
                        izpisi=False):

    # =======================
    # Prispevki (za pokojninsko in invalidsko zavarovanje)
    # =======================
    # Zaposleni:  21.1%
    prispevki = bruto_zasluzek * 0.221

    # =======================
    # Davčne olajšave (letno)
    # =======================
    # 1. Splošna olajšava
    znesek_splosna_olajsava = splosna_olajsava(bruto_zasluzek)

    # 2. Osebne olajsave za 100% invalide
    znesek_olajsava_za_invalide = 17658.84 if invalid else 0

    # 3. Posebna osebna olajšava
    # Ne pride v poštev za zaposlene (samo za študente in dijake)

    # 4. Posebna olajšava
    # 4.1 za vzdrževane otroke
    olajsava_za_vzdrzevane_otroke = olajsava_vzdrzevani_otroci(
        stevilo_vzdrzevanih_otrok) * (stevilo_vzdrzevanih_mesecev/12)
    # 4.2za vsakega drugega vzdrževanega družinskega člana
    olajsava_za_vzdrzevane_druzinske_clane = olajsava_vzdrzevani_druzinski_clani(
        stevilo_vzdrzevanih_druzinskih_clanov) * (stevilo_vzdrzevanih_mesecev/12)

    # 5. Olajšava za prostovoljno dodatno pokojninsko zavarovanje
    # Največ do zneska premije, ki je enak 24 % obveznih prispevkov za
    # pokojninsko in invalidsko zavarovanje za zavarovanca
    # Oziroma 5,844% pokojnine zavarovanca
    znesek_olajsava_za_dodatno_pokojnino = min(
        premija_dod_pok_zav, 0.24 * prispevki)
    # Ne več kot 2.819,09 eurov letno.
    znesek_olajsava_za_dodatno_pokojnino = min(
        znesek_olajsava_za_dodatno_pokojnino, 2819.09)

    # =======================
    # Poračun
    # =======================
    olajsave = znesek_splosna_olajsava \
        + znesek_olajsava_za_invalide \
        + olajsava_za_vzdrzevane_otroke \
        + olajsava_za_vzdrzevane_druzinske_clane \
        + znesek_olajsava_za_dodatno_pokojnino

    # Neto letna davčna osnova
    neto_davcna_osnova = bruto_zasluzek - prispevki - olajsave
    # Omejimo se na pozitivne vsote
    neto_davcna_osnova = max(neto_davcna_osnova, 0)

    # Stopnja dohodnine (letno)
    letna_dohodnina = letna_dohodnina_lestvica(neto_davcna_osnova)

    if izpisi:
        print(f"Bruto letni zaslužek: {bruto_zasluzek:.2f}€")
        print(f"Prispevki: {prispevki:.2f}€")
        print(f"Olajšave skupaj: {olajsave:.2f}€")
        print(f"Neto letna davčna osnova: {neto_davcna_osnova:.2f}€")
        print(f"Letna dohodnina: {letna_dohodnina:.2f}€")
        print(
            f"Neto letni zaslužek: {(bruto_zasluzek - prispevki -letna_dohodnina):.2f}€")

    return letna_dohodnina


def main():
    print("***| Informativni izracun dohodnine za zaposlenega |***")
    bruto_letni_zasluzek = float(input("Vnesite svoj bruto letni zasluzek: "))

    invalid = input(
        "Ste invalid s 100% telesno okvaro? (y/N): ").lower() == 'y'

    stevilo_vzdrzevanih_otrok = int(input(
        "Število vzdrževanih otrok (starost <18) (0-?): "))
    stevilo_vzdrzevanih_druzinskih_clanov = int(input(
        "Število vzdrževanih družinskih članov (starost 18-26) (0-?): "))
    if stevilo_vzdrzevanih_otrok > 0 or stevilo_vzdrzevanih_druzinskih_clanov > 0:
        stevilo_vzdrzevanih_mesecev = int(
            input("Število mesecev (starost 18-26) (0-12): "))
    else:
        stevilo_vzdrzevanih_mesecev = 12

    premija_dod_pok_zav = float(
        input("Letni znesek premije za dodatno pokojninsko zavarovanje (v eur): "))

    print("\nInformativni izračun: \n")

    izracunaj_dohodnino(
        bruto_zasluzek=bruto_letni_zasluzek,
        invalid=invalid,
        stevilo_vzdrzevanih_otrok=stevilo_vzdrzevanih_otrok,
        stevilo_vzdrzevanih_druzinskih_clanov=stevilo_vzdrzevanih_druzinskih_clanov,
        stevilo_vzdrzevanih_mesecev=stevilo_vzdrzevanih_mesecev,
        premija_dod_pok_zav=premija_dod_pok_zav,
        izpisi=True
    )


if __name__ == "__main__":
    main()
