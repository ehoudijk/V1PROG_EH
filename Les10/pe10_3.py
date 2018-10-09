gebruiker = 'Rutte'
beginstation = 'Alkmaar'
eindstation = 'Den Helder'

def myfunc(x,y,z):
    insert = x + y + z
    output = ''
    for i in insert:
        encode = ord(i)
        output += chr((encode+3))
    print(output)

myfunc(gebruiker, beginstation, eindstation)
