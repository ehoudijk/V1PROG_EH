def acronym(input):
    'returns acronym of input string'
    words = input.split()
    res = ''
    for word in words:
        res = res + word[0].upper()
    return res

acro = acronym('utrecht science park')
print(acro)