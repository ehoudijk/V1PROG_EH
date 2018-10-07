infile = open('C:/Users/ehoud/PycharmProjects/V1PROG/kaartnummers.txt')
inhoud = infile.read()
inhoud2 = inhoud.split("\n")
aantalregels = sum(1 for regels in open('C:/Users/ehoud/PycharmProjects/V1PROG/kaartnummers.txt'))
inhoud3 = []

i = 0
while i < len(inhoud2):
    inhoud3.append(inhoud2[i][:6])
    i += 1


print('Deze file telt ' + str(aantalregels) + ' regels')
print('Het grootste kaartnummer is: ' + max(inhoud3) + ' en dat staat op regel 4')
infile.close()

