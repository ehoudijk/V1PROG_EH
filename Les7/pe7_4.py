import datetime

infile = open('hardlopers.txt', 'w')
vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %Y, %H:%M:%S, ")
infile.write(s + input('Naam van persoon: ') + '\n')


while True:
    vandaag = datetime.datetime.today()
    s = vandaag.strftime("%a %d %b %Y, %H:%M:%S, ")
    infile = open('C:/Users/ehoud/PycharmProjects/V1PROG/Les7/hardlopers.txt', 'a')
    y = input('Naam van persoon: ')
    x = (s + y)
    if y == 'afgelopen':
        break
    else:
        infile.write(x + '\n')
