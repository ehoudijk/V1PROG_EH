oud = 'test1234'

def new_password(oldpassword, newpassword):
    if len(newpassword) >= 6 and newpassword != oldpassword:
        print('Nieuw wachtwoord ingesteld')
    else:
        print('Ongeldig wachtwoord')

nieuw = input('Geef een nieuw wachtwoord: ')

new_password(oud, nieuw)
