from collections import Counter
from util.cnpjApi import CnpjApi
import csv
from PyQt5 import uic, QtWidgets, QtGui

app = QtWidgets.QApplication([])
tela = uic.loadUi("ui/main.ui")
#x = ["11003135000127", "00394502000144", "42498725000363"]


def init():
    inputCnpj = tela.inputCnpj.toPlainText()
    listCnpj = inputCnpj.replace(" ", ",").replace(",", ",")
    statusBar = False
    # ZERA VALORES ANTES DE PROCESSAR
    tela.progressBar.setValue(0)
    tela.lcdComplete.display(0)
    tela.lcdErros.display(0)

    if len(listCnpj) == 0:
        tela.inputCnpj.setText("Necessário um CNPJ")
    else:
        listMCnpj = []
        listMCnpj = listCnpj.split(",")
        listCSV = []
        listErros = []

        for x in Counter(listMCnpj):
            cnpj = CnpjApi(x)
            """Validação de erros"""
            if cnpj.validate() == True:
                listCSV.append(cnpj.getJson())
                tela.lcdComplete.display(len(listCSV))
            else:
                """ADICIONA ERROS AO CSV"""
                listErros.append(x)
                tela.lcdErros.display(len(listErros))
                with open('erros.csv', 'w', newline='') as file:
                    writer = csv.writer(
                        file, quoting=csv.QUOTE_ALL, delimiter=';')
                    writer.writerows(listErros)

            """STATUS BAR"""
            tela.progressBar.setValue(
                tela.progressBar.value() + 10)

        """ADICIONA LISTA AO CSV"""
        with open('cnpj.csv', 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL, delimiter=';')
            writer.writerows(listCSV)

    """SET 100% NO STATUS BAR"""
    statusBar = True
    if statusBar == True:
        tela.progressBar.setValue(100)


"""CONFIGURAÇOES DE TELA"""
tela.buttonStart.clicked.connect(init)
tela.lbComplete.setPixmap(QtGui.QPixmap("img/complete.png"))
tela.lbErro.setPixmap(QtGui.QPixmap("img/erro.png"))

tela.lbComplete.setScaledContents(True)
tela.lbErro.setScaledContents(True)

tela.show()
app.exec_()


"""11003135000127 00394502000144 42498725000363
    longitude latitude, simei e insc estadual
"""
