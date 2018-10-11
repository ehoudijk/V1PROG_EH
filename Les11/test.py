import datetime
import csv

with open('inloggers.csv', 'a', newline='') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')
    writer.writerow(('naam', 'voorl', 'gbdatum', 'email'))

    while True:
        vandaag = datetime.datetime.today()
        naam = input("Wat is je achternaam? ")

        if naam == 'einde':
            break

        else:
            voorl = input("Wat zijn je voorletters? ")
            gbdatum = input("Wat is je geboortedatum? ")
            email = input("Wat is je e-mail adres? ")

        writer.writerow('naam', 'voorl', 'gbdatum', 'email')

    # '%a %d %B %Y at %H:%M;'
