# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'text_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("快递信息识别")
        Dialog.resize(668, 375)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(230, 10, 201, 31))
        self.label.setStyleSheet("font: 14pt \"Agency FB\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(10, 60, 301, 291))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.video1 = QtWidgets.QLabel(self.frame)
        self.video1.setGeometry(QtCore.QRect(3, 1, 301, 291))
        self.video1.setText("")
        self.video1.setObjectName("video1")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(340, 60, 311, 301))
        self.textBrowser.setObjectName("textBrowser")
        self.listView = QtWidgets.QListView(Dialog)
        self.listView.setGeometry(QtCore.QRect(0, 0, 670, 377))
        self.listView.setMinimumSize(QtCore.QSize(670, 377))
        self.listView.setMaximumSize(QtCore.QSize(670, 377))
        self.listView.setStyleSheet("background-image:url(:/BG_text.png)")
        self.listView.setObjectName("listView")
        self.listView.raise_()
        self.label.raise_()
        self.frame.raise_()
        self.textBrowser.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "快递信息识别"))
        self.label.setText(_translate("Dialog", "快递信息识别"))
import data.resources_rc
