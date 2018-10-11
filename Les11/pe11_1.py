def kostenverdeling(kosten):
    intaantal = None
    while intaantal is None:
        try:
            straantal = input('Het aantal personen: ')
            intaantal = int(straantal)
            kostenpp = kosten / intaantal
            if intaantal < 0:
                print('{} - Negatieve getallen zijn niet toegestaan!'.format(intaantal))
                intaantal = None
                break
        except ValueError:
            print('Gebruik cijfers voor het invoeren van het aantal!')
            break
        except ZeroDivisionError:
            print('Delen door nul kan niet!')
            break
        except:
            print('Onjuiste invoer!')
            break
        print(kostenpp)


kosten = 4356
kostenverdeling(kosten)
