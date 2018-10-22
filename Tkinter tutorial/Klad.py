print('Dit zijn de vertrekkende treinen:')

for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        eindbestemming = vertrek['EindBestemming']

        vertrektijd = vertrek['VertrekTijd']
        vertrektijd = vertrektijd[11:16]

        return 'Om {} vertrekt de {} vanaf spoor {} naar {}.'.format(vertrektijd, vertrek['TreinSoort'], vertrek['VertrekSpoor']['#text'], eindbestemming)

print(aanvrager('Gouda'))


----

def stations():
    vertrekstation = station_entry.get()
    res = aanvrager('Gouda')


    for vertrek in res['ActueleVertrekTijden']['VertrekkendeTrein']:
        eindbestemming = vertrek['EindBestemming']

        vertrektijd = vertrek['VertrekTijd']
        vertrektijd = vertrektijd[11:16]

        x =  'Om {} vertrekt de {} vanaf spoor {} naar {}.'.format(vertrektijd, vertrek['TreinSoort'], vertrek['VertrekSpoor']['#text'], eindbestemming)

    label["text"] = x
