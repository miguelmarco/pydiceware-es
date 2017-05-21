#! /usr/bin/python

from PyQt5 import QtCore, QtGui, QtWidgets, uic
try:
    from crypto.Random import random
except:
    from Crypto.Random import random
import pickle
import sys
from math import log, ceil
import pkg_resources

def leepalabras():
    f = open('palabras.txt')
    dic = {}
    for l in f:
        if ':' in l:
            palabra = l[:-2]
            dic[palabra]=[]
        else:
            dic[palabra].append(l[:-1])
    return dic


class Programa(QtWidgets.QDialog):
    def __init__(self, parent = None):
        QtWidgets.QDialog.__init__(self)
        self.ui = uic.loadUi("generapass.ui")
        self.ui.show()

    def genera(self, *args):
        bits = int(self.ui.spinBox.value())
        keyword = str(self.ui.lineEdit.text())
        bitsusados = 0
        length = int(self.ui.spinBox_2.value())
        self.ui.textBrowser.clear()
        if keyword:
            bits_disponibles = [log(len(dic[a]),2) for a in keyword]
            totalbits = sum(bits_disponibles)
            for letra in keyword.lower():
                b = bits_disponibles.pop(0)
                aelegir = int(ceil(2**(bits*b/totalbits)))
                palabras = dic[letra][:aelegir]
                n = random.choice(palabras)
                self.ui.textBrowser.insertPlainText(n+'\n')
                bitsusados += log(len(palabras),2)
        else:
            aelegir = int(ceil(2**(float(bits)/length)))
            palabras = dic['all'][:aelegir]
            for i in range(length):
                n = random.choice(palabras)
                self.ui.textBrowser.insertPlainText(n+'\n')
                bitsusados += log(len(palabras),2)
        self.ui.statusbar.showMessage('bits de entropia: ' + str(bitsusados))



if __name__ == "__main__":
    dic = leepalabras()
    app = QtWidgets.QApplication(sys.argv)
    window = Programa()
    window.ui.pushButton.clicked.connect(window.genera)
    sys.exit(app.exec_())
