def standaardtarief(afstandKM):
    if afstandKM <= 0:
        return '€0.00'
    elif afstandKM <= 50:
        return afstandKM * 80
    elif afstandKM > 50:
        return (afstandKM * 60) + 1500


KMinvoer = -1
tarief = standaardtarief(KMinvoer)
print(tarief)

KMinvoer = 0
tarief = standaardtarief(KMinvoer)
print(tarief)

KMinvoer = 50
tarief = standaardtarief(KMinvoer)
print(tarief)

KMinvoer = 51
tarief = standaardtarief(KMinvoer)
print(tarief)