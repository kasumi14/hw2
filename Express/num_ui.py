# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'num_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("快递编号识别")
        Dialog.resize(588, 335)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(200, 10, 181, 31))
        self.label_2.setStyleSheet("font: 14pt \"Agency FB\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 141, 21))
        self.label_3.setStyleSheet("font: 12pt \"Agency FB\";")
        self.label_3.setObjectName("label_3")
        self.listView = QtWidgets.QListView(Dialog)
        self.listView.setGeometry(QtCore.QRect(-10, 0, 601, 431))
        self.listView.setStyleSheet("background-image:url(:/BG_num.png)")
        self.listView.setObjectName("listView")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 90, 591, 241))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 591, 241))
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(150, 60, 421, 21))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 411, 21))
        self.label_4.setStyleSheet("font: 15pt \"Agency FB\";")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.listView.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.frame.raise_()
        self.frame_2.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "快递编码识别"))
        self.label_2.setText(_translate("Dialog", "快递编码识别"))
        self.label_3.setText(_translate("Dialog", "识别到的快递编码："))
        self.label_4.setText(_translate("Dialog", "xxxx xxxx xxxx xxxx"))
import data.resources_rc