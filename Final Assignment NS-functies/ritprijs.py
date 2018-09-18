def standaardtarief(afstandKM):
    if afstandKM <= 0:
        return '€0.00'
    elif afstandKM <= 50:
        return afstandKM * 80
    elif afstandKM > 50:
        return (afstandKM * 60) + 1500

KMinvoer = 50
tarief = standaardtarief(KMinvoer)
print(tarief)

def ritprijs(leeftijd, weekendrit, tarief):
    if (leeftijd <12 or leeftijd > 64) and weekendrit == False:
        return int(tarief * 0.7) #30% korting
    elif (leeftijd <12 or leeftijd > 64) and weekendrit == True:
        return int(tarief * 0.65) #35% korting
    elif (leeftijd > 11 and leeftijd < 65) and weekendrit == False:
        return int(tarief * 1) #geen korting
    elif (leeftijd > 11 and leeftijd < 65) and weekendrit == True: #leeftijdsvergelijkingen kunnen geschreven als 11 < leeftijd < 65
        return int(tarief * 0.6) #40% korting

leeftijd = 64
weekendrit = True
prijs = ritprijs(leeftijd, weekendrit, tarief)
print(prijs)
