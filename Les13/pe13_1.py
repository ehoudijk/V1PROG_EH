import xmltodict

def xmlreader(filename):
    with open(filename) as myxml:
        inhoudxml = myxml.read()
        xmldict = xmltodict.parse(inhoudxml)
        return xmldict


x = 'C:/Users/ehoud/Dropbox/Studie/Vakken/Blok A/Programming TICT-V1PROG-15/artikelen.xml'
y = xmlreader(x)
res = y['artikelen']['artikel']


for artikel in res:
    print(artikel['naam'])
