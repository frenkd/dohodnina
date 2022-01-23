from student import izracunaj_dohodnino as dohodnina_student
from zaposlen import izracunaj_dohodnino as dohodnina_zaposlen

def main():
    print("\n***| Informativni izračun dohodnine za celotno družino |***")
    bruto_letni_zasluzek_prvi_stars = float(input("Bruto letni zaslužek prvega starša: "))
    bruto_letni_zasluzek_drugi_stars = float(input("Bruto letni zaslužek drugega starša: "))
    bruto_letni_zasluzek_student = float(input("Bruto letni zaslužek študenta: "))

    stevilo_vzdrzevanih_druzinskih_clanov = int(input("Število dodatnih vzdrževanih družinskih članov (brez študenta) (>18 let)) (0-?): "))
    stevilo_vzdrzevanih_otrok = int(input("Število dodatnih vzdrževanih otrok (<18 let) (0-?): "))

    stevilo_vzdrzevanih_mesecev_prvi_stars = int(input("Število vzdrževanih mesecev prvega starša (0-12): "))

    print("\nInformativni izračun:\n")

    # ==============================================
    # Upoštevanje studenta kot vzdrzevanega druzinskega clana

    # Prvi starš
    prvi_stars_1 = dohodnina_zaposlen(
        bruto_zasluzek=bruto_letni_zasluzek_prvi_stars,
        stevilo_vzdrzevanih_druzinskih_clanov=stevilo_vzdrzevanih_druzinskih_clanov+1,
        stevilo_vzdrzevanih_otrok=stevilo_vzdrzevanih_otrok,
        stevilo_vzdrzevanih_mesecev=stevilo_vzdrzevanih_mesecev_prvi_stars,
        izpisi=False
    )

    # Drugi starš
    drugi_stars_1 = dohodnina_zaposlen(
        bruto_zasluzek=bruto_letni_zasluzek_drugi_stars,
        stevilo_vzdrzevanih_druzinskih_clanov=stevilo_vzdrzevanih_druzinskih_clanov+1,
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
        stevilo_vzdrzevanih_druzinskih_clanov=stevilo_vzdrzevanih_druzinskih_clanov,
        stevilo_vzdrzevanih_otrok=stevilo_vzdrzevanih_otrok,
        stevilo_vzdrzevanih_mesecev=stevilo_vzdrzevanih_mesecev_prvi_stars,
        izpisi=False
    )

    # Drugi starš
    drugi_stars_2 = dohodnina_zaposlen(
        bruto_zasluzek=bruto_letni_zasluzek_drugi_stars,
        stevilo_vzdrzevanih_druzinskih_clanov=stevilo_vzdrzevanih_druzinskih_clanov,
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
        f"Skupna dohodnina s prijavo študenta kot vzdrževanega družinskega člana: {skupna_dohodnina_1:.2f}€")
    print(
        f"Skupna dohodnina brez prijave študenta kot vzdrževanega družinskega člana: {skupna_dohodnina_2:.2f}€")
    print(f"Razlika: {razlika:.2f}€")

    if razlika < 0:
        print("Študenta SE SPLAČA prijaviti kot vzdrževanega družinskega člana")
    else:
        print("Študenta se NE SPLAČA prijaviti kot vzdrževanega družinskega člana")


if __name__ == "__main__":
    main()

