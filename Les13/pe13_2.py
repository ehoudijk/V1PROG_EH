def verdubbelB(x):
    global b
    b = x + x


b = 7
verdubbelB(b)

print(b)

_________


import time

print(time.strftime("%H:%M:%S"))

_________


def f(y):
   return 2*y + 1


def g(x):
   return 5 + x + 10


print(f(3)+g(3))
