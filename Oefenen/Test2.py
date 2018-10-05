import re


def teller(x):
    t = open(x)
    inhoud = t.read()
    inhoud2 = re.split(", |\\n",inhoud)
    aantalregels = sum(1 for regels in open('x'))
    print(aantalregels)



infile = open('C:/Users/ehoud/PycharmProjects/V1PROG/kaartnummers.txt')
inhoud = infile.read()


#inhoud2 = re.split(", |\\n",inhoud)
aantalregels = sum(1 for regels in open('C:/Users/ehoud/PycharmProjects/V1PROG/kaartnummers.txt'))


teller()
print(inhoud2)
print(aantalregels)
print(len(inhoud2))
