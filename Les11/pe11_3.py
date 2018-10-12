import csv

with open('gamers.csv', 'r') as myCSVFile:

    reader = csv.reader(myCSVFile, delimiter=';')

    currenthighest = 0
    for row in reader:
        score = int(row[2])
        if score > currenthighest:
            currenthighest = score
            date = row[1]
            name = row[0]
    print('De hoogste score is: {} op {} behaald door {}'.format(score, date, name))
