def kwadraten_som(grondgetallen):
    for i in grondgetallen:
        return [i**2 for i in grondgetallen if i > 0]


lijst = [4, 5, 3, -81]
print(kwadraten_som(lijst))