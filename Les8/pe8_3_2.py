class opmaak:
   BOLD = '\033[1m'
   END = '\033[0m'

invoer = "5-9-7-1-7-8-3-2-4-8-7-9"

sorteer = invoer.split('-')

for i in range(0, len(sorteer)):
    sorteer[i] = int(sorteer[i])


print(opmaak.BOLD + 'Gesorteerde list van ints: ' + str(sorted(sorteer)) + opmaak.END)
print(opmaak.BOLD + 'Grootste getal: ' + str(max(sorteer)) + ' en Kleinste getal: ' + str(min(sorteer)) + opmaak.END)
print(opmaak.BOLD + 'Aantal getallen: ' + str(len(sorteer)) + ' en Som van de getallen: ' + str(sum(sorteer)) + opmaak.END)
print(opmaak.BOLD + 'Gemiddelde: ' + str((sum(sorteer)/len(sorteer))) + opmaak.END)
