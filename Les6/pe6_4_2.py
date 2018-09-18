import re

def new_password(oldpassword, newpassword):
    if len(newpassword) < 6:
        print('Het nieuwe wachtwoord moet minstens 6 karakters bevatten waarvan minimaal 1 cijfer.')
    elif newpassword == oldpassword:
        print('Het nieuwe wachtwoord mag niet gelijk zijn aan het oude wachtwoord.')
    elif re.search('[0-9]', newpassword) is None:
        print('Het nieuwe wachtwoord moet een cijfer bevatten.')
    else:
        print('Het nieuwe wachtwoord is geaccepteerd.')

oud = 'test1234'
nieuw = input('Geef een nieuw wachtwoord: ')

new_password(oud, nieuw)
