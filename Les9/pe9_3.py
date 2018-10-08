cijferscursus = {'Henk': 97, 'Iris': 50, 'Bastiaan': 20, 'Maxwell': 60, 'Yvette': 93, 'Tessa': 95, 'Bob': 75, 'Eric': 99}  # dictionary voor het gemak onder elkaar geschreven. Cijfers in een score uit 100 opschrijven om ze als int te kunne gebruiken


def excelleren(invoer):
    for i in invoer.items():
        if i[1] > int(90):
            print(str(i[0]), (i[1]/10))


excelleren(cijferscursus)


