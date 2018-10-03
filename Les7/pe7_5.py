def gemiddelde(gemzin):
    zinsplit = gemzin.split(" ")
    x = 0
    for i in range(len(zinsplit)):
        x += len(zinsplit[i])
    print(x / len(zinsplit))


gemiddelde(input('Uw willekeurige zin: '))
