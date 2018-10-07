

def kluis_openen():
    aantal = kluizen.readlines()
    x = [i.split(';') for i in aantal]
    kluisnum = input('geef uw kluisnummer: ')
    kluisww = input('geef uw wachtwoord: ')
    for g in x:
        if kluisnum == x[g][0] and kluisww == x[g][1]:
            print('Dat is correct')
        else:
            print('Geen geldige combinatie van kluisnummer en wachtwoord')


kluizen = open('kluizen.txt', 'r+')  # openen text file
kluis_openen()

aantal = kluizen.readlines()
x = [i.split(';') for i in aantal]
kluisnum = input('geef uw kluisnummer: ')
kluisww = input('geef uw wachtwoord: ')
for g in x:
    if kluisnum in x[g] and kluisww in x[g]:
        print('yes')
        kluizen.close()
    else:
        print('bs')