#abro la interfaz de la GUI
from GUI_ui import Ui_Dialog
from PySide2.QtWidgets import QApplication, QDialog
import sys

class modeloGui():
    def __init__(self):
        self.app = QApplication()
        self.Dialog = QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()
        sys.exit(self.app.exec_())
        



if __name__ == "__main__":
    app = QApplication()
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())