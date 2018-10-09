bruin = {'boxtel', 'best', 'beukenlaan', 'eindhoven', 'helmond \'t hout', 'helmond', 'helmond brouwhuis', 'deurne'}
groen = {'boxtel', 'best', 'beukenlaan', 'eindhoven', 'geldrop', 'heeze', 'weert'}

print(bruin & groen)  # welke plaatsen komen op beide trajecten voor
print(bruin - groen)  # welke plaatsen doet bruin aan, maar niet groen
print(bruin | groen)  # alle plaatsen op beide trajecten
