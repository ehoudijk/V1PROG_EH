import re


infile = open('C:/Users/ehoud/PycharmProjects/V1PROG/kaartnummers.txt')
inhoud = infile.read()


inhoud2 = re.split(", |\\n",inhoud)
aantalregels = sum(1 for regels in open('C:/Users/ehoud/PycharmProjects/V1PROG/kaartnummers.txt'))
print(inhoud2)
print(aantalregels)
print(len(inhoud2))
