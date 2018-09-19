def standaardtarief(afstandKM):
    if afstandKM <= 0:
        return 0
        print('€0.00')
    elif afstandKM <= 50:
        return afstandKM * 80
    elif afstandKM > 50:
        return (afstandKM * 60) + 1500


def ritprijs(leeftijd, weekendrit, afstandKM):
    if (leeftijd <12 or leeftijd > 64) and weekendrit is False:
        return int(standaardtarief(afstandKM) * 0.7)
    elif (leeftijd <12 or leeftijd > 64) and weekendrit is True:
        return int(standaardtarief(afstandKM) * 0.65)
    elif (11 < leeftijd < 65) and weekendrit is False:
        return int(standaardtarief(afstandKM) * 1)
    elif (11 < leeftijd < 65) and weekendrit is True:  # leeftijdscomp simpeler als 11 < leeftijd < 65
        return int(standaardtarief(afstandKM) * 0.6)  # 40% korting


afstandKM = 10
leeftijd = 11
weekendrit = True

print("€{0:.2f}".format((ritprijs(leeftijd, weekendrit, afstandKM)/100)))
