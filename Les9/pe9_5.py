def namen():
    namen = {}

    while True:
        naam = input('Geef een naam: ')
        if len(naam) > 0:
            if naam in namen:
                namen[naam] += 1
            else:
                namen[naam] = 1
        else:
            break

    for naam in namen:
        if namen[naam] == 1:
            print('Er is {} student met de naam {}'.format(namen[naam], naam))
        else:
            print('Er zijn {} studenten met de naam {}'.format(namen[naam], naam))

#    for key, value in namen.items():
#        if value == 1:
#            print('Er is 1 student met de naam {}'.format(key))
#        else:
#            print('Er zijn {} studenten met de naam {}'.format(value,key))


namen()
