import csv

with open('newfile.csv', 'w', newline='') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')
    writer.writerow(('number', 'name'))

    while True:
        name = input('Name? ')

        if name == '':
            break

        number = input('Number? ')

        writer.writerow((number, name))
