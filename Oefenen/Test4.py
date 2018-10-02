import datetime
vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %Y, %H:%M:%S, ")
print(s + input('Naam van persoon: '))