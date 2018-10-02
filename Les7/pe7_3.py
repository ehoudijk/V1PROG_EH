invoer = "5-9-7-1-7-8-3-2-4-8-7-9"

sorteer = invoer.split('-')

for i in range(0, len(sorteer)):
    sorteer[i] = int(sorteer[i])


print('Gesorteerde list van ints: ' + str(sorted(sorteer)))  #ter controle
print('Grootste getal: ' + str(max(sorteer)) + ' en Kleinste getal: ' + str(min(sorteer)))
print('Aantal getallen: ' + str(len(sorteer)) + ' en Som van de getallen: ' + str(sum(sorteer)))
print('Gemiddelde: ' + str((sum(sorteer)/len(sorteer))))
