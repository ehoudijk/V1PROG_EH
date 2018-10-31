def inlezen_beginstation(stations):
    """Deze funtie vraagd om het beginstation en controleerd of deze op het traject bestaat"""
    while True:
        start = input('Geef uw vertrekstation: ')  # overbodig
        if start.lower() in stations:
            return start
        else:
            print('Dit station zit niet op deze lijn.')
            continue


def inlezen_eindstation(stations, beginstation):
    """Deze funtie vraagd om het eindstation en controleerd of deze op het traject bestaat, en of het beginstation voor het eindstation komt"""
    while True:
        eind = input('Geef uw eindstation: ')
        if eind.lower() not in stations:
            print('Deze trein komt niet in {}.'.format(eind))
            continue
        else:
            if stations.index(beginstation) < stations.index(eind):
                return eind
            else:
                print('Deze trein komt niet in ' + eind)
                continue


def omroepen_reis(stations, beginstation, eindstation):
    """Deze functie print de resultaten. Het beginstation, eindstation, de afstand en de prijs"""
    beginnr = stations.index(beginstation)
    eindnr = stations.index(eindstation)
    afstand = stations.index(eindstation) - stations.index(beginstation)
    prijs = 5 * afstand
    print('Het beginstation {} is het {}e station in het traject.'.format(beginstation, beginnr))
    print('Het eindstation {} is het {}e station in het traject.'.format(eindstation, eindnr))
    print('De afstand bedraagd {} station(s).'.format(afstand))
    print('De prijs van het kaartje is {} euro.'.format(prijs))
    print('Jij stapt in de trein in: {}'.format(beginstation))
    for i in range((beginnr+1), eindnr):
        print(' - {}'.format(stations[i]))
    print('Jij stapt uit in: {}'.format(eindstation))


stations = ['schagen', 'heerhugowaard', 'alkmaar', 'castricum', 'zaandam', 'amsterdam sloterdijk', 'amsterdam centraal', 'amsterdam amstel', 'utrecht centraal', 's-hertogenbosch', 'weert', 'roermond', 'sittard', 'maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)
