# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegistroDepar.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RegistroDepar(object):
    def setupUi(self, RegistroDepar):
        RegistroDepar.setObjectName("RegistroDepar")
        RegistroDepar.resize(553, 180)
        self.buttonBox = QtWidgets.QDialogButtonBox(RegistroDepar)
        self.buttonBox.setGeometry(QtCore.QRect(30, 140, 331, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(RegistroDepar)
        self.label.setGeometry(QtCore.QRect(160, 0, 241, 71))
        self.label.setStyleSheet("font: 20pt \"Sitka Display\";")
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(RegistroDepar)
        self.widget.setGeometry(QtCore.QRect(30, 60, 511, 71))
        self.widget.setObjectName("widget")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 211, 41))
        self.label_4.setStyleSheet("font: 12pt \"Sitka Display\";")
        self.label_4.setObjectName("label_4")
        self.textEdit_NombreDepar = QtWidgets.QTextEdit(self.widget)
        self.textEdit_NombreDepar.setGeometry(QtCore.QRect(240, 20, 251, 31))
        self.textEdit_NombreDepar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_NombreDepar.setObjectName("textEdit_NombreDepar")

        self.retranslateUi(RegistroDepar)
        self.buttonBox.accepted.connect(RegistroDepar.accept)
        self.buttonBox.rejected.connect(RegistroDepar.reject)
        QtCore.QMetaObject.connectSlotsByName(RegistroDepar)

    def retranslateUi(self, RegistroDepar):
        _translate = QtCore.QCoreApplication.translate
        RegistroDepar.setWindowTitle(_translate("RegistroDepar", "Dialog"))
        self.label.setText(_translate("RegistroDepar", "DEPARTAMENTO"))
        self.label_4.setText(_translate("RegistroDepar", "Nombre:"))
        self.textEdit_NombreDepar.setHtml(_translate("RegistroDepar", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

import decorativos_rc
