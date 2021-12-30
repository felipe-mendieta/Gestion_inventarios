# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaAcercaDe.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AcercaDe(object):
    def setupUi(self, AcercaDe):
        AcercaDe.setObjectName("AcercaDe")
        AcercaDe.resize(820, 444)
        AcercaDe.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2 = QtWidgets.QLabel(AcercaDe)
        self.label_2.setGeometry(QtCore.QRect(0, 340, 821, 101))
        self.label_2.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(AcercaDe)
        self.textBrowser.setGeometry(QtCore.QRect(400, 20, 411, 311))
        self.textBrowser.setStyleSheet("color: rgb(0, 0, 255);\n"
"font: 13pt \"Courier New\";")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textBrowser.setReadOnly(True)
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(AcercaDe)
        self.label.setGeometry(QtCore.QRect(30, 60, 341, 101))
        self.label.setStyleSheet("border-image: url(:/Fondos/Recursos/escudofinal.png);")
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(AcercaDe)
        QtCore.QMetaObject.connectSlotsByName(AcercaDe)

    def retranslateUi(self, AcercaDe):
        _translate = QtCore.QCoreApplication.translate
        AcercaDe.setWindowTitle(_translate("AcercaDe", "Form"))
        self.textBrowser.setHtml(_translate("AcercaDe", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Courier New\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">1.0.0</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">Sistema de gestión de activos realizado por Felipe Mendieta, estudiante de Ingeniería de sistemas de la Universidad de Cuenca.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://www.ucuenca.edu.ec\"><span style=\" text-decoration: underline; color:#ffffff;\">https://www.ucuenca.edu.ec</span></a></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p></body></html>"))

import decorativos_rc
