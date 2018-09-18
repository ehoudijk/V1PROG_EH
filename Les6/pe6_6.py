import re

oud = 'test1234'

def new_password(oldpassword, newpassword):
    if newpassword != oldpassword:
        print('Het nieuwe wachtwoord mag niet gelijk zijn aan het oude wachtwoord.')
    else:
        print('Het nieuwe wachtwoord is geaccepteerd.')

nieuw = input('Geef een nieuw wachtwoord: ')

new_password(oud, nieuw)
