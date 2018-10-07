studentencijfers = [[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]]

def gemiddelde_per_student(studentencijfers):
    student = 0
    lst_gemiddelde_student = []
    tijdelijke_opslag = []
    for cijfers in studentencijfers:
        gemiddelde = int(sum(cijfers) / 3)
        student += 1
        x = 'student %a heeft een gemiddelde van %a' % (student, gemiddelde)
        lst_gemiddelde_student.append(x)
        tijdelijke_opslag.append(x)
    print(tijdelijke_opslag)
    return tijdelijke_opslag


def gemiddelde_van_alle_studenten(studentencijfers):
    totaal = 0
    for student in studentencijfers:
        gem = int(sum(student)) / len(student)
        totaal = totaal + gem
        totgem = totaal / len(studentencijfers)
    print('Het gemiddelde van alle studenten is: %.2f' % (totgem))
    return totgem



gemiddelde_per_student(studentencijfers)
gemiddelde_van_alle_studenten(studentencijfers)
