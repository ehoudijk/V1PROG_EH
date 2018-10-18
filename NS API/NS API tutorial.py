import requests
import xmltodict

auth_details = ('eric.houdijk@student.hu.nl', 'CTgaWBynYE_wm6Yy6j-BAykLFoVLA4cKChnuMIWuejiMdISQbUHRRw')
api_url = ('http://webservices.ns.nl/ns-api-avt?station={}'.format(input('Wat is uw vertrekstation? ')))
response = requests.get(api_url, auth=auth_details)

vertrekXML = xmltodict.parse(response.text)
print('Dit zijn de vertrekkende treinen:')

for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
    eindbestemming = vertrek['EindBestemming']

    vertrektijd = vertrek['VertrekTijd']
    vertrektijd = vertrektijd[11:16]

    print('Om {} vertrekt de {} vanaf spoor {} naar {}.'.format(vertrektijd, vertrek['TreinSoort'], vertrek['VertrekSpoor']['#text'], eindbestemming))
