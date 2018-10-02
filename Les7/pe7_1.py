def convert(tempc):
    fahrenheit = int(tempc) * 1.8 + 32
    return fahrenheit

def table(tempcon):
    print('   F    C')
    formatStr = '{:5} {:5}'
    for i in range(-30, 50, 10):
        print(formatStr.format(convert(i), float(i)))


table(0)
