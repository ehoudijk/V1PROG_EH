import xmltodict

def xmlreader(filename):
    with open(filename) as myxml:
        inhoudxml = myxml.read()
        xmldict = xmltodict.parse(inhoudxml)
        return xmldict


file = xmlreader('stations')

print('Dit zijn de codes en types van de 4 stations:')  # code en type
for i in range(4):
    print('{:4s}'.format(file['Stations']['Station'][i]['Code']) + ' - ' + (file['Stations']['Station'][i]['Type']))

print('\nDit zijn alle stations met één of meer synoniemen:')
for i in range(4):
    if str(file['Stations']['Station'][i]['Synoniemen']) == 'None':
        pass
    else:
        print('{:4s}'.format(file['Stations']['Station'][i]['Code']) + ' - ' + str(file['Stations']['Station'][i]['Synoniemen']['Synoniem']))

print('\nDit is de lange naam van elk station:')
for i in range(4):
    print('{:4s}'.format(file['Stations']['Station'][i]['Code']) + ' - ' + (file['Stations']['Station'][i]['Namen']['Lang']))



#    print(file['Stations']['Station'][i]['Code'] + ' - ' + (file['Stations']['Station'][i]['Type']))

#print('Dit zijn de codes en types van de 4 stations:')
#print((file['Stations']['Station'][0]['Code']) + ' - ' + (file['Stations']['Station'][0]['Type']))
#print((file['Stations']['Station'][1]['Code']) + ' - ' + (file['Stations']['Station'][1]['Type']))
#print((file['Stations']['Station'][2]['Code']) + ' - ' + (file['Stations']['Station'][2]['Type']))
#print((file['Stations']['Station'][3]['Code']) + ' - ' + (file['Stations']['Station'][3]['Type']))


#print(file['Stations']['Station'][1]['Code'])