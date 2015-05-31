import os
from unidecode import unidecode
import pickle

files = os.listdir('./')
files = [a for a in files if 'txt' in a]

from unidecode import unidecode

diccios = {'all':{}}

for f in files:
    print f
    fil = open(f)
    for l in fil:
        for w in l.split():
            w = unidecode(w.decode('utf8'))
            if w.isalpha():
                wo = w.lower()
                wo = str(unidecode(wo.decode('latin1')))
                letra = wo[0]
                if not letra in diccios:
                    diccios[letra] = {}
                if wo in diccios['all']:
                    diccios['all'][wo] += 1
                else:
                    diccios['all'][wo] = 1
                if wo in diccios[letra]:
                    diccios[letra][wo] += 1
                else:
                    diccios[letra][wo] = 1
    fil.close()
    print [(i,len(diccios[i])) for i in diccios]


diccionario = {letra:list(reversed(sorted(diccios[letra], key = lambda a: diccios[letra][a]))) for letra in diccios.keys()}
f = open('diccionarios.obj','w')
pickle.dump(diccionario,f,2)
f.close()
diceware = sorted(diccionario['all'][:7776])
f = open('diceware.txt','w')
for i in range(7776):
    st = ''
    n = i
    for j in range(5):
        st =  str(n%6 + 1) + st
        n = n/6
    st += ' ' + diceware[i] + '\n'
    f.write(st)
f.close()
