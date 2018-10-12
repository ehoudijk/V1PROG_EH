import csv

with open('artikelen.csv', 'w', newline='') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')
    writer.writerow(('Artikelnummer', 'Artikelcode', 'Naam', 'Voorraad', 'Prijs'))

    while True:
        artikelnummer = input('Geef het artikelnummer: ')
        if artikelnummer == '':
            break
        artikelcode = input('Geef de artikelcode: ')
        naam = input('Geef de naam van het artikel: ')
        voorraad = input('Geef het aantal nog op voorraad zijnde artikelen: ')
        prijs = input('Geef de prijs van het artikel: ')
        writer.writerow((artikelnummer, artikelcode, naam, voorraad, prijs))
