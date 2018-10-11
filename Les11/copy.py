import datetime
import csv


bestand = open('inloggers.csv')

while True:
    text = open(bestand, 'a')
    naam = input("Wat is je achternaam? ")
    if naam == 'einde':
        text.close()
        break
    else:
        voorl = input("Wat zijn je voorletters? ")
        gbdatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mail adres? ")
        vandaag = datetime.datetime.today()
        x = vandaag.strftime("%a %d %B %Y at %H:%M;{};{};{};{}\n".format(naam, voorl, gbdatum, email))
        text.write(x)
        text.close()
