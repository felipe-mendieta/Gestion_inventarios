# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegistroContacto.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RegistroContacto(object):
    def setupUi(self, RegistroContacto):
        RegistroContacto.setObjectName("RegistroContacto")
        RegistroContacto.resize(551, 241)
        RegistroContacto.setStyleSheet("background-image: url(:/Fondos/Recursos/fondo13.jpg);")
        self.buttonBox = QtWidgets.QDialogButtonBox(RegistroContacto)
        self.buttonBox.setGeometry(QtCore.QRect(130, 200, 231, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.widget = QtWidgets.QWidget(RegistroContacto)
        self.widget.setGeometry(QtCore.QRect(0, 70, 531, 121))
        self.widget.setObjectName("widget")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 211, 41))
        self.label_4.setStyleSheet("font: 12pt \"Sitka Display\";")
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(10, 60, 211, 41))
        self.label_7.setStyleSheet("font: 12pt \"Sitka Display\";")
        self.label_7.setObjectName("label_7")
        self.textEdit_Nombre = QtWidgets.QTextEdit(self.widget)
        self.textEdit_Nombre.setGeometry(QtCore.QRect(270, 20, 251, 31))
        self.textEdit_Nombre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_Nombre.setObjectName("textEdit_Nombre")
        self.textEdit_Telf = QtWidgets.QTextEdit(self.widget)
        self.textEdit_Telf.setGeometry(QtCore.QRect(270, 70, 251, 31))
        self.textEdit_Telf.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_Telf.setObjectName("textEdit_Telf")
        self.label = QtWidgets.QLabel(RegistroContacto)
        self.label.setGeometry(QtCore.QRect(190, 0, 161, 71))
        self.label.setStyleSheet("font: 20pt \"Sitka Display\";")
        self.label.setObjectName("label")

        self.retranslateUi(RegistroContacto)
        self.buttonBox.accepted.connect(RegistroContacto.accept)
        self.buttonBox.rejected.connect(RegistroContacto.reject)
        QtCore.QMetaObject.connectSlotsByName(RegistroContacto)

    def retranslateUi(self, RegistroContacto):
        _translate = QtCore.QCoreApplication.translate
        RegistroContacto.setWindowTitle(_translate("RegistroContacto", "Dialog"))
        self.label_4.setText(_translate("RegistroContacto", "Nombre:"))
        self.label_7.setText(_translate("RegistroContacto", "Teléfono:"))
        self.textEdit_Nombre.setHtml(_translate("RegistroContacto", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_Telf.setHtml(_translate("RegistroContacto", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("RegistroContacto", "CONTACTO"))

import decorativos_rc
