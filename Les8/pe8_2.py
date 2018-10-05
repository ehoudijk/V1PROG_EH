#s = eval(input("Geef een lijst met minimaal 10 strings: "))
s = ["boter", "kaas", "bier", "pizza", "thee", "drop", "koek", "cola", "boterham", "stamppot"]

def stringsort(x):
    s4 = []
    for i in range(len(s)):
        while int(len(s[i])) == x:
            s4.append(s[i])
            break
    print(s4)


stringsort(4)

