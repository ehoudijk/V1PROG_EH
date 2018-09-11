cijferICOR = 7.0
cijferPROG = 9.0
cijferCSN = 8.0
gemiddelde = ((cijferPROG + cijferICOR + cijferCSN) / 3)
beloning = ((cijferCSN + cijferICOR + cijferPROG) * 30)
overzicht = 'Hard werken wordt beloond. Mijn cijfers (gemiddeld een ' + str(gemiddelde) + ' ) leveren een beloning van €' + str(beloning) + ' op!'
print(overzicht)