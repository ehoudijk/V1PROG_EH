def seizoen(maand):
    if maand < 3 or maand > 11:
        print('Winter')
    elif maand > 8:
        print('Herfst')
    elif maand > 5:
        print('Zomer')
    else:
        print('Lente')


seizoen(9)
