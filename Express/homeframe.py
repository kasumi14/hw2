from PyQt5 import QtWidgets, QtGui, QtCore
from Express.homeui import Ui_Dialog
from Express.text_conframe import TextDialog
from Express.num_conframe import NumDialog
class HomeDialog(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QtWidgets.QLabel(self)
        self.setCentralWidget(self.label)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
    def go_text(self):
        self.text_conframe = TextDialog()
        self.text_conframe.show()
        self.close()
    def go_num(self):
        self.num_conframe = NumDialog()
        self.num_conframe.show()
        self.close()
