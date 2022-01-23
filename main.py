from student import main as student_main
from zaposlen import main as zaposlen_main

if __name__ == "__main__":
    student = input("Ste študent? (y/N): ").lower() == 'y'

    if student:
        student_main()
    else:
        zaposlen_main()
