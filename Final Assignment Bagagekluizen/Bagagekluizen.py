def toon_keuze_kluizen_vrij():
    'toont het aantal vrije kluizen'
    beschikbaar = 12 - len(keuze)
    if beschikbaar <= 0:
        vrij = 'Er zijn geen kluizen meer beschikbaar\n'
    elif beschikbaar == 1:
        vrij = 'Er is nog 1 kluis beschikbaar\n'
    else:
        vrij = ('Er zijn {} kluizen beschikbaar\n'.format(beschikbaar))

    print(vrij)


def nieuwe_kluis():
    'laat iemand een nieuwe kluis aanvragen en een code opgeven'
    nummering = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    vergeven = []
    kluizen = open('kluizen.txt', 'r+')
    aantal = kluizen.readlines()
    for regel in aantal:
        nummers = regel.split(';')
        cijfers = int(nummers[0])
        vergeven.append(cijfers)

    for kluis in vergeven:
        nummering.remove(kluis)

    if len(nummering) > 0:
        print('Er zijn nog vrije kluizen over.')
        wachtwoord = input('Wachtwoord: ')
        kluizen.write('{};{}\n'.format(nummering[0], wachtwoord))
        kluizen.close()
        print('Uw kluisnummer is: ' + str(nummering[0]))
    else:
        kluizen.close()
        print('geen kluis meer beschikbaar')


def kluis_openen():
    """hiermee kan een kluis geopent worden"""
    aantal = kluizen.readlines()
    x = [i.split(';') for i in aantal]
    kluisnum = input('geef uw kluisnummer: ')
    kluisww = input('geef uw wachtwoord: ')
    for i in x:
        if x[0][0] == kluisnum and x[0][1] == kluisww:
            print('Dat is correct')
        else:
            print('Geen geldige combinatie van kluisnummer en wachtwoord')


kluizen = open('kluizen.txt', 'r+')  # openen text file
keuze = kluizen.readlines()  # inlezen text file


while True:
    'Keuzemenu'
    print("1: Ik wil weten hoeveel kluizen nog vrij zijn. \n2: Ik wil een nieuwe kluis.\n3: Ik wil even iets uit mijn kluis halen.\n5: Ik wil stoppen\n")
    keuze = str(input("Toets het nummer van uw keuze: " '\n'))
    if keuze == '1':
        toon_keuze_kluizen_vrij()
        continue
    elif keuze == '2':
        nieuwe_kluis()
        continue
    elif keuze == '3':
        kluis_openen()
        continue
    elif keuze == '5':
        print('Het programma stopt')
        break
    else:
        print('Probeer opnieuw')
        continue


kluizen.close()  # sluiten text file
