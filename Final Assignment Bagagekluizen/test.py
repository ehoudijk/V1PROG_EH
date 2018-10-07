def kluis_openen():
    kluizen = open('kluizen.txt', 'r+')
    aantal = kluizen.readlines()
    nraantal = len(aantal)
    teller = 0
    x = [i.split(';') for i in aantal]
    kluisnum = input('geef uw kluisnummer: ')
    kluisww = input('geef uw wachtwoord: ')
    for g in range(len(x)):
        if x[g][0] == kluisnum and x[g][1] == (kluisww + '\n'):
            print('Dat is correct')
            break
        else:
            teller += 1
            if teller == nraantal:
                print('Geen geldige combinatie van kluisnummer en wachtwoord')
    kluizen.close()

kluis_openen()
