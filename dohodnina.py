def letna_dohodnina_lestvica(neto_letna_davcna_osnova):
    """Izracuna letno neto dohodnino glede na lestvico"""
    n = neto_letna_davcna_osnova
    if n < 8500.00:
        return n * 0.16
    elif n < 25000.00:
        return 1360.00 + (n - 8500.00) * 0.26
    elif n < 50000.00:
        return 5650.00 + (n - 25000.00) * 0.33
    elif n < 72000.00:
        return 13900.00 + (n - 50000.00) * 0.39
    else:
        return 22480.00 + (n - 72000.00) * 0.50


def splosna_olajsava(skupni_dohodek):
    """Višina skupne splošne olajšave je odvisna od višine skupnega dohodka v letu"""
    if skupni_dohodek < 13316.83:
        return 3500.00 + (18700.38 - 1.40427 * skupni_dohodek)
    else:
        return 3500.00


def olajsava_vzdrzevani_otroci(stevilo_vzdrzevanih_otrok):
    """Izračun olajšave glede na število vzdrževanih otrok (<18 let)"""
    olajsava = 0

    if stevilo_vzdrzevanih_otrok >= 1:
        olajsava = olajsava + 2436.92
    if stevilo_vzdrzevanih_otrok >= 2:
        olajsava = olajsava + 2649.24
    if stevilo_vzdrzevanih_otrok >= 3:
        olajsava = olajsava + 4418.54
    if stevilo_vzdrzevanih_otrok >= 4:
        olajsava = olajsava + 6187.85
    if stevilo_vzdrzevanih_otrok >= 5:
        olajsava = olajsava + 7957.14

    # Za vse nadaljnje vzdrževane otroke se višina olajšave poveča za 1.769,30 eura
    # (mesečno za 147,44 eura) glede na višino olajšave za predhodnega vzdrževanega otroka.
    zadnji_otrok = 7957.14
    for _ in range(stevilo_vzdrzevanih_otrok-5):
        olajsava = olajsava + zadnji_otrok
        zadnji_otrok = zadnji_otrok + 1769.30

    return olajsava


def olajsava_vzdrzevani_druzinski_clani(stevilo_vzdrzevanih_druzinskih_clanov):
    """Izracun olajsave glede na stevilo vzdrzevanih druzinskih clanov"""
    return stevilo_vzdrzevanih_druzinskih_clanov * 2436.92
