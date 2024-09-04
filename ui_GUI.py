# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUIcjCyCN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import json
import sys
#importo el metodo abrirCase desde model.py
from model import modelo
m= modelo()
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(597, 473)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 10, 81, 31))
        self.pushButton.clicked.connect(self.abrirCase)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 16, 341, 20))
        self.comboBox = QComboBox(Dialog)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 80, 101, 22))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 50, 101, 31))
        self.comboBox_2 = QComboBox(Dialog)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(10, 140, 101, 22))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 110, 61, 31))
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 180, 121, 31))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 220, 61, 20))
        self.retranslateUi(Dialog)
        #abro el json en la carpeta json de nombre jsonHysys.json
        jsonGUI=json.load(open("json/jsonHysys.json"))
        #############################################
        #configuro los botones y los textos de la GUI
        #############################################
        if self.label.text() == "Default":
            self.label.setText(jsonGUI["direccionCase"])
        else:
            self.label.setText(jsonGUI["direccionCase"])
        #del primer combobox agarro el texto que está seteado
        #si está vacío, agrego el nombre de la corriente de proceso
        #si no, lo cambio por el nombre de la corriente de proceso
        if self.comboBox.currentText()=="":
            self.comboBox.addItem(jsonGUI["corrienteProceso"]["nombre"])
        else:
            self.comboBox.setItemText(0,jsonGUI["corrienteProceso"]["nombre"])
        if self.comboBox_2.currentText() == "":
            self.comboBox_2.addItem(jsonGUI["corrienteServicio"]["nombre"])
        else:
            self.comboBox_2.setItemText(0,jsonGUI["corrienteServicio"]["nombre"])
        
        QMetaObject.connectSlotsByName(Dialog)

    def abrirCase(self):
        #abro una widget para seleccionar un archivo y extraer si direccion para abrirlo
        self.dialog = QFileDialog()
        self.dirCase=self.dialog.getOpenFileName()[0] #direccion del case que voy a abrir.
        #guardo la direccion del case en un json
        self.jsonGUI=json.load(open("json/jsonHysys.json"))
        self.jsonGUI["direccionCase"]=self.dirCase
        #guardo la direccion del case en un json
        with open("json/jsonHysys.json","w") as file:
            json.dump(self.jsonGUI,file)
        m.abrirCase_m()


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Abrir case", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Default", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Corriente de proceso", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Propiedades", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Mostrar propiedad ", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Default", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

