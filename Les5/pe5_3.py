age = eval(input('Geef je leeftijd: '))
nlpp = input('Nederlands paspoort Ja/Nee: ')

if age > 17 and nlpp == 'Ja':
    print('Gefeliciteerd, je mag stemmen!')

elif age < 18:
    print('Je bent nog te jong om te stemmen.')

elif nlpp != 'Ja':
    print('Alleen Nederlanders mogen stemmen.')