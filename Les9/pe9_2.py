while True:
    woord = input('Geef een string van vier letters: ')
    woordlen = len(woord)
    if woordlen == 4:
        print('Inlezen van correcte string: ' + woord + ' is geslaagd')
        break
    else:
        print(woord + ' heeft ' + str(woordlen) + ' letters')
