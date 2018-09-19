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


distance = eval(input('Hoeveel KM ga je reizen? '))
age = eval(input('Wat is jouw leeftijd? '))
weekend = input('Reis je in het weekend (Ja/Nee)? ')

while (weekend != 'Ja') and (weekend != 'Nee'):
    print('Antwoord met Ja of Nee')
    weekend = input('Reis je in het weekend (Ja/Nee)? ')

if weekend == 'Ja':
    weekend = True
if weekend == 'Nee':
    weekend = False

print("€{0:.2f}".format((ritprijs(age, weekend, distance) / 100)))
