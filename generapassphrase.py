#!/usr/bin/python
from Crypto.Random import random
import pickle
import sys
from math import log, ceil

args = sys.argv[1:]
if '-b' in args:
    n = args.index('-b')
    args.pop(n)
    bits = int(args.pop(n))
else:
    bits = 60
if '-l' in args:
    n = args.index('-l')
    args.pop(n)
    length = int(args.pop(n))
else:
    length = 5
if len(args)>0:
    keyword = args[0].lower()
else:
    keyword = False

f = open('diccionarios.obj', 'r')
dic = pickle.load(f)
f.close()

bitsusados = 0

if keyword:
    bits_disponibles = [log(len(dic[a]),2) for a in keyword]
    totalbits = sum(bits_disponibles)
    for letra in keyword.lower():
        b = bits_disponibles.pop(0)
        aelegir = int(ceil(2**(bits*b/totalbits)))
        palabras = dic[letra][:aelegir]
        n = random.choice(palabras)
        print n
        bitsusados += log(len(palabras),2)
else:
    aelegir = int(ceil(2**(float(bits)/length)))
    palabras = dic['all'][:aelegir]
    for i in range(length):
        n = random.choice(palabras)
        print n
        bitsusados += log(len(palabras),2)

print 'bits de entropia: ' + str(bitsusados)
