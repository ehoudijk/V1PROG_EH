def convert(tempc):
    fahrenheit = int(tempc) * 1.8 + 32
    return fahrenheit

def table(minimum, maximum, stap):
    print('   F    C')
    formatStr = '{:5} {:5}'
    for i in range(minimum, maximum, stap):
        print(formatStr.format(convert(i), float(i)))


table(-30, 50, 10)