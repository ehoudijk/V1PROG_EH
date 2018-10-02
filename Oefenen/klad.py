def acronym(input):
    """returns acronym of input string"""
    words = input.split()
    res = ''
    for word in words:
        res = res + word[0].upper()
    return res


acro = acronym('utrecht science park')
print(acro)


def nested(n):
    for j in range(n):
        for i in range(n):
            print(i, end=' ')
        print()


n = 5
nested(n)


def nested(n):
    for j in range(n):
        for i in range(j+1):
            print(i, end=' ')
        print()


n = 5
nested (n)