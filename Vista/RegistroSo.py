# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegistroSo.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RegistroSo(object):
    def setupUi(self, RegistroSo):
        RegistroSo.setObjectName("RegistroSo")
        RegistroSo.resize(552, 300)
        RegistroSo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.buttonBox = QtWidgets.QDialogButtonBox(RegistroSo)
        self.buttonBox.setGeometry(QtCore.QRect(150, 240, 221, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(RegistroSo)
        self.label.setGeometry(QtCore.QRect(130, 0, 301, 71))
        self.label.setStyleSheet("font: 20pt \"Sitka Display\";\n"
"color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(RegistroSo)
        self.widget.setGeometry(QtCore.QRect(0, 60, 521, 171))
        self.widget.setObjectName("widget")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 211, 41))
        self.label_4.setStyleSheet("font: 12pt \"Sitka Display\";\n"
"color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(10, 60, 211, 41))
        self.label_5.setStyleSheet("font: 12pt \"Sitka Display\";\n"
"")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(10, 110, 211, 41))
        self.label_6.setStyleSheet("font: 12pt \"Sitka Display\";\n"
"")
        self.label_6.setObjectName("label_6")
        self.textEdit_NomSO = QtWidgets.QTextEdit(self.widget)
        self.textEdit_NomSO.setGeometry(QtCore.QRect(280, 20, 241, 31))
        self.textEdit_NomSO.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_NomSO.setObjectName("textEdit_NomSO")
        self.textEdit_VersSO = QtWidgets.QTextEdit(self.widget)
        self.textEdit_VersSO.setGeometry(QtCore.QRect(280, 70, 241, 31))
        self.textEdit_VersSO.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_VersSO.setObjectName("textEdit_VersSO")
        self.textEdit_DescSO = QtWidgets.QTextEdit(self.widget)
        self.textEdit_DescSO.setGeometry(QtCore.QRect(280, 120, 241, 31))
        self.textEdit_DescSO.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_DescSO.setObjectName("textEdit_DescSO")

        self.retranslateUi(RegistroSo)
        self.buttonBox.accepted.connect(RegistroSo.accept)
        self.buttonBox.rejected.connect(RegistroSo.reject)
        QtCore.QMetaObject.connectSlotsByName(RegistroSo)

    def retranslateUi(self, RegistroSo):
        _translate = QtCore.QCoreApplication.translate
        RegistroSo.setWindowTitle(_translate("RegistroSo", "Dialog"))
        self.label.setText(_translate("RegistroSo", "SISTEMA OPERATIVO"))
        self.label_4.setText(_translate("RegistroSo", "Nombre:"))
        self.label_5.setText(_translate("RegistroSo", "Versión:"))
        self.label_6.setText(_translate("RegistroSo", "Descripción:"))
        self.textEdit_NomSO.setHtml(_translate("RegistroSo", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_VersSO.setHtml(_translate("RegistroSo", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_DescSO.setHtml(_translate("RegistroSo", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

import decorativos_rc
