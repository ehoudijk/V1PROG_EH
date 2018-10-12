import csv

with open('artikelen.csv', 'r') as myCSVFile:

    reader = csv.reader(myCSVFile, delimiter=';')

    currenthighest = 0
    totaalvoorraad = 0
    currentsmallest = 10000
    firstline = True
    for row in reader:  # zorgt ervoor dat de eerste regel, de header, overgeslagen wordt.
        if firstline:
            firstline = False
            continue
        price = eval(row[4])
        hoeveelheid = eval(row[3])
        totaalvoorraad += eval(row[3])
        if int(price) > currenthighest:
            currenthighest = price
            name = row[2]
        if int(hoeveelheid) < currentsmallest:
            currentsmallest = hoeveelheid
            artknr = row[0]


print('Het duurste artikel is {} en die kost {} Euro'.format(name, "%.2f" % currenthighest))
print('Er zijn slechts {} exemplaren in voorraad van het product met nummer {}'.format(currentsmallest, artknr))
print('In totaal hebben wij {} producten in ons magazijn liggen'.format(totaalvoorraad))
