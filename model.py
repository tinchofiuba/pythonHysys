
from PyQt5.QtWidgets import QApplication, QDialog
import sys
import os
import json
from hysys2Python import abrir

class modelo():
    def __init__(self):
        #creo una señalpara vincularme con la UI
        case="s1"
        corrientes="s2"
        propiedades="s3"

    def abrirCase_m(self):
        #en función de la dirección seleccionada en la GUI (guardado en un json) abro el case
        #leo jsonHysys.json y lo llego a un diccionario
        self.jsonModel = json.load(open("json/jsonHysys.json"))
        self.dirCase=self.jsonModel["direccionCase"]
        abrir(self.dirCase)

    def mostrarCorrientes(self):
        print("mostrar corrientes")

    def mostrarPropiedades(self):
        print("mostrar propiedad")

if __name__ == "__main__":
    app = QApplication()
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    #aplico las modificaciones de modelo gui
    modelo=modelo()
    sys.exit(app.exec_())