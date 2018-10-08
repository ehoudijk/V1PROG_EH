filepath = 'C:/Users/ehoud/PycharmProjects/V1PROG/Les9/tickersymbol'
tickers = {}
tickersrev = {}

def ticker(filename):
    text = open(filename)
    lijn = text.readlines()
    key = []
    value = []

    for i in lijn:
        x = i.strip('\n')
        y = x.split(':')
        key.append(y[0])
        value.append(y[1])

    for i in range(len(key)):
        tickers[key[i]] = value[i]
        tickersrev[value[i]] = key[i]
    text.close()
    return tickers, tickersrev


def zoekfunctie(filepath):
    print('1. Bedrijfsnaam zoeken \n2. Bedrijfsticker zoeken')
    invoer = input('Kies 1 of 2: ')
    ticker(filepath)

    if int(invoer) == 1:
        invoer1 = input('Ticker: ')
        print('Enter Company name: ' + tickersrev[invoer1] + '\nTicker symbol: ' + invoer1)
    else:
        invoer2 = input('Bedrijfsnaam: ')
        print('Enter Company name: ' + invoer2 + '\nTicker symbol: ' + tickers[invoer2])


zoekfunctie(filepath)


#    if int(invoer) == 1:
#        invoer1 = input('Ticker: ')
#        for i in tickers:
#            if tickers.values(i) == str(invoer1):
#                print(i.tickers)
