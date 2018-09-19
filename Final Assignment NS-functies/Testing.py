def standaardtarief(afstandkm):
    if afstandkm <= 0:
        return 0
    elif afstandkm <= 50:
        return afstandkm * 80
    elif afstandkm > 50:
        return (afstandkm * 60) + 1500


def ritprijs(leeftijd, weekendrit, afstandkm):
    if (leeftijd < 12 or leeftijd > 64) and weekendrit is False:
        return int(standaardtarief(afstandkm) * 0.7)
    elif (leeftijd < 12 or leeftijd > 64) and weekendrit is True:
        return int(standaardtarief(afstandkm) * 0.65)
    elif (11 < leeftijd < 65) and weekendrit is False:
        return int(standaardtarief(afstandkm) * 1)
    elif (11 < leeftijd < 65) and weekendrit is True:
        return int(standaardtarief(afstandkm) * 0.6)


afstandkm = eval(input('Hoeveel KM ga je reizen? '))
leeftijd = eval(input('Wat is jouw leeftijd? '))
weekendrit = input('Reis je in het weekend (Ja/Nee)? ')

while (weekendrit != 'Ja') and (weekendrit != 'Nee'):
    print('Antwoord met Ja of Nee')
    weekendrit = input('Reis je in het weekend (Ja/Nee)? ')

if weekendrit == 'Ja':
    weekendrit = True
if weekendrit == 'Nee':
    weekendrit = False

print("€{0:.2f}".format((ritprijs(leeftijd, weekendrit, afstandkm) / 100)))
