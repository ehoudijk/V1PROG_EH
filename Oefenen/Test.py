def standaardtarief(afstandKM):
    if afstandKM <= 0:
        return '€0.00'
    elif afstandKM <= 50:
        return afstandKM * 80
    elif afstandKM > 50:
        return (afstandKM * 60) + 1500


def ritprijs(leeftijd, weekendrit, afstandKM):
    if (leeftijd <12 or leeftijd > 64) and weekendrit is False:
        return int(standaardtarief(afstandKM) * 0.7)
    elif (leeftijd <12 or leeftijd > 64) and weekendrit is True:
        return int(standaardtarief(afstandKM) * 0.65) #35% korting
    elif (leeftijd > 11 and leeftijd < 65) and weekendrit is False:
        return int(standaardtarief(afstandKM) * 1) #geen korting
    elif (leeftijd > 11 and leeftijd < 65) and weekendrit is True: #leeftijdsvergelijkingen kunnen geschreven als 11 < leeftijd < 65
        return int(standaardtarief(afstandKM) * 0.6) #40% korting



afstandKM = 50
leeftijd = 67
weekendrit = False

print(ritprijs(leeftijd, weekendrit, afstandKM))

