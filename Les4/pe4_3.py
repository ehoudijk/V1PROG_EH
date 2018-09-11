loon = eval(input('Wat verdien je per uur: '))
uren = eval(input('Hoeveel uur heb je gewerkt: '))
verdiend = str(uren) + ' uur werken levert ' + str((uren*loon)) + ' Euro op'
print(verdiend)

#str zet er vitrueel ' ' omheen. de variabele uren en loon worden als int geladen en verrekend
#en daarna verwerkt tot str die het moet zijn om als tekst behandeld te worden voor print functie