import requests
import xmltodict


def aanvrager(vertrekstation):
    auth_details = ('eric.houdijk@student.hu.nl', 'CTgaWBynYE_wm6Yy6j-BAykLFoVLA4cKChnuMIWuejiMdISQbUHRRw')
    api_url = ('http://webservices.ns.nl/ns-api-avt?station={}'.format(vertrekstation))
    response = requests.get(api_url, auth=auth_details)

    vertrekXML = xmltodict.parse(response.text)
    antwoord = []

    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        eindbestemming = vertrek['EindBestemming']

        vertrektijd = vertrek['VertrekTijd']
        vertrektijd = vertrektijd[11:16]

        antwoord.append('Om {} vertrekt de {} vanaf spoor {} naar {}.\n'.format(vertrektijd, vertrek['TreinSoort'], vertrek['VertrekSpoor']['#text'], eindbestemming))

    return antwoord
