from student import izracunaj_dohodnino as dohodnina_student
from zaposlen import izracunaj_dohodnino as dohodnina_zaposlen

# Zasluzki
bruto_letni_zasluzek_prvi_stars = 40000  # Prvi stars zasluzi 40k bruto letno
bruto_letni_zasluzek_drugi_stars = 30000  # Drugi stars zasluzi 30k bruto letno

# Otroci
stevilo_vzdrzevanih_otrok = 1  # Eden izmed otrok je mladoleten
stevilo_vzdrzevanih_druzinskih_clanov = 1  # Eden pa je student

# Ker ima prvi stars vecji bruto zasluzek, se splaca pisati
# vse vzdrzevane mesce otrok in vzdrzevanih clanov nanj (če že)
# Poskusite tudi obratno! Lahko tudi vsak po 6 mesecev!
stevilo_vzdrzevanih_mesecev_prvi_stars = 12

# ==== Možnost #1
# Recimo da študent dela med vikendi v baru
# 8 ur, 2 dni na teden, 40 tednov v letu, 8e/h bruto
# = 5200 eur bruto
bruto_letni_zasluzek_student = 5200

# ==== Možnost #2
# Recimo da študent dela v firmi part-time med študijem, ki plača nadpovprečno
# 4 ure, 5 dni na teden, 40 tednov v letu, 12e/h bruto
# = 9600 eur bruto
# bruto_letni_zasluzek_student = 4 * 5 * 40 * 12

# ==== Možnost #3
# Recimo da študent dela v full-time med absolventom za firmo, ki plača zelo nadpovprečno
# 8 ur, 5 dni na teden, 40 tednov v letu, 16e/h bruto
# = 25600 eur bruto
# bruto_letni_zasluzek_student = 8 * 5 * 40 * 16

# ==============================================
# Upoštevanje studenta kot vzdrzevanega druzinskega clana

# Prvi starš
prvi_stars_1 = dohodnina_zaposlen(
    bruto_zasluzek=bruto_letni_zasluzek_prvi_stars,
    stevilo_vzdrzevanih_druzinskih_clanov=stevilo_vzdrzevanih_druzinskih_clanov,
    stevilo_vzdrzevanih_otrok=stevilo_vzdrzevanih_otrok,
    stevilo_vzdrzevanih_mesecev=stevilo_vzdrzevanih_mesecev_prvi_stars,
    izpisi=False
)

# Drugi starš
drugi_stars_1 = dohodnina_zaposlen(
    bruto_zasluzek=bruto_letni_zasluzek_drugi_stars,
    stevilo_vzdrzevanih_druzinskih_clanov=stevilo_vzdrzevanih_druzinskih_clanov,
    stevilo_vzdrzevanih_mesecev=12-stevilo_vzdrzevanih_mesecev_prvi_stars,
    izpisi=False
)

# Študent
student_1 = dohodnina_student(
    bruto_zasluzek=bruto_letni_zasluzek_student,
    prijavljen_kot_vzdrzevan=True,
    stroski_prevoza_in_nocitve=0,
    izpisi=False
)


# ==============================================
# Brez upostevanja studenta

# Prvi starš
prvi_stars_2 = dohodnina_zaposlen(
    bruto_zasluzek=bruto_letni_zasluzek_prvi_stars,
    stevilo_vzdrzevanih_druzinskih_clanov=stevilo_vzdrzevanih_druzinskih_clanov-1,
    stevilo_vzdrzevanih_otrok=stevilo_vzdrzevanih_otrok,
    stevilo_vzdrzevanih_mesecev=stevilo_vzdrzevanih_mesecev_prvi_stars,
    izpisi=False
)

# Drugi starš
drugi_stars_2 = dohodnina_zaposlen(
    bruto_zasluzek=bruto_letni_zasluzek_drugi_stars,
    stevilo_vzdrzevanih_druzinskih_clanov=stevilo_vzdrzevanih_druzinskih_clanov-1,
    stevilo_vzdrzevanih_otrok=stevilo_vzdrzevanih_otrok,
    stevilo_vzdrzevanih_mesecev=12-stevilo_vzdrzevanih_mesecev_prvi_stars,
    izpisi=False
)

# Študent
student_2 = dohodnina_student(
    bruto_zasluzek=bruto_letni_zasluzek_student,
    prijavljen_kot_vzdrzevan=False,
    stroski_prevoza_in_nocitve=0,
    izpisi=False
)

skupna_dohodnina_1 = prvi_stars_1 + drugi_stars_1 + student_1
skupna_dohodnina_2 = prvi_stars_2 + drugi_stars_2 + student_2
razlika = skupna_dohodnina_1 - skupna_dohodnina_2

print(
    f"Skupna dohodnina s prijavo studenta kot vzdrzevanega druzinskega clana: {skupna_dohodnina_1}")
print(
    f"Skupna dohodnina brez prijave studenta kot vzdrzevanega druzinskega clana: {skupna_dohodnina_2}")
print(f"Razlika: {razlika}")

if razlika < 0:
    print("Študenta SE SPLAČA prijaviti kot vzdrževanega družuinskega člana")
else:
    print("Študenta se NE SPLAČA prijaviti kot vzdrževanega družuinskega člana")
