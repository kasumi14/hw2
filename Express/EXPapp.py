from PyQt5.QtWidgets import QApplication
from Express.homeframe import HomeDialog
import sys

class Expapp(QApplication):
    def __init__(self):
        super(Expapp, self).__init__(sys.argv)
        self.dialog = HomeDialog()
        self.dialog.show()