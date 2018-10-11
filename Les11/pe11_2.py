import datetime
import csv

with open('inloggers.csv', 'a', newline='') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')

    while True:
        naam = input("Wat is je achternaam? ")

        if naam == 'einde':
            break

        else:
            voorl = input("Wat zijn je voorletters? ")
            gbdatum = input("Wat is je geboortedatum? ")
            email = input("Wat is je e-mail adres? ")
            vandaag = datetime.datetime.today()
            x = vandaag.strftime('%a %d %B %Y at %H:%M')
            writer.writerow((x, naam, voorl, gbdatum, email))
