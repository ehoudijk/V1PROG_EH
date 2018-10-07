#counter = 0
#while True:
#    getal = eval(input('Geef een getal: '))
#    if getal != 0:
#        counter += 1
#    else:
#        print('Er zijn ' + str(counter) + ' getallen ingevoerd')
#        break

counter = 0
som = 0
while True:
    getal = eval(input('Geef een getal: '))
    if getal == 0:
        break
    counter += 1
    som += int(getal)
print('Er zijn ' + str(counter) + ' getallen ingevoerd, de som is: ' + str(som))
