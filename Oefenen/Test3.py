def standaardtarief(afstandKM):
    if afstandKM <= 0:
        return 0
    elif afstandKM <= 50:
        return afstandKM * 80
    elif afstandKM > 50:
        return (afstandKM * 60) + 1500


def ritprijs(leeftijd, weekendrit, afstandKM):
    if (leeftijd <12 or leeftijd > 64) and weekendrit is 'Nee':
        return int(standaardtarief(afstandKM) * 0.7)
    elif (leeftijd <12 or leeftijd > 64) and weekendrit is 'Ja':
        return int(standaardtarief(afstandKM) * 0.65)
    elif (11 < leeftijd < 65) and weekendrit is 'Nee':
        return int(standaardtarief(afstandKM) * 1)
    elif (11 < leeftijd < 65) and weekendrit is 'Ja':  # leeftijdscomp simpeler als 11 < leeftijd < 65
        return int(standaardtarief(afstandKM) * 0.6)  # 40% korting


afstandKM = eval(input('Hoeveel KM ga je reizen? '))
leeftijd = eval(input('Wat is jouw leeftijd? '))
#weekendrit = (input('Reis je in het weekend (Ja/Nee)? ') == 'Ja')
weekendrit = input('Reis je in het weekend (Ja/Nee)? ')
if weekendrit == 'Ja':
    print("€{0:.2f}".format((ritprijs(leeftijd, weekendrit, afstandKM) / 100)))
#print('Antwoord met Ja of Nee')




#print("€{0:.2f}".format((ritprijs(leeftijd, weekendrit, afstandKM)/100)))
