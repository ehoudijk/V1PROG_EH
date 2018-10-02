infile = open('C:/Users/ehoud/PycharmProjects/V1PROG/kaartnummers.txt')
inhoud = infile.read()
infile.close()


import re


inhoud2 = re.split(", |\\n",inhoud)

i = 0
while i < len(inhoud2):
    print(inhoud2[(i + 1)] + " heeft kaartnummer: " + inhoud2[(i)])
    i += 2


