# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegistroConfigTip.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RegistroConfigTip(object):
    def setupUi(self, RegistroConfigTip):
        RegistroConfigTip.setObjectName("RegistroConfigTip")
        RegistroConfigTip.resize(547, 411)
        RegistroConfigTip.setStyleSheet("background-image: url(:/Fondos/Recursos/fondo13.jpg);")
        self.buttonBox = QtWidgets.QDialogButtonBox(RegistroConfigTip)
        self.buttonBox.setGeometry(QtCore.QRect(90, 360, 271, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(RegistroConfigTip)
        self.label.setGeometry(QtCore.QRect(110, 0, 321, 71))
        self.label.setStyleSheet("font: 20pt \"Sitka Display\";")
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(RegistroConfigTip)
        self.widget.setGeometry(QtCore.QRect(0, 80, 521, 271))
        self.widget.setObjectName("widget")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 211, 41))
        self.label_4.setStyleSheet("font: 12pt \"Sitka Display\";")
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
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(10, 170, 211, 41))
        self.label_7.setStyleSheet("font: 12pt \"Sitka Display\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(10, 220, 211, 41))
        self.label_8.setStyleSheet("font: 12pt \"Sitka Display\";\n"
"color: rgb(0, 0, 0);")
        self.label_8.setObjectName("label_8")
        self.textEdit_DescConfT = QtWidgets.QTextEdit(self.widget)
        self.textEdit_DescConfT.setGeometry(QtCore.QRect(270, 20, 251, 31))
        self.textEdit_DescConfT.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_DescConfT.setObjectName("textEdit_DescConfT")
        self.textEdit_MarcConfT = QtWidgets.QTextEdit(self.widget)
        self.textEdit_MarcConfT.setGeometry(QtCore.QRect(270, 70, 251, 31))
        self.textEdit_MarcConfT.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_MarcConfT.setObjectName("textEdit_MarcConfT")
        self.textEditModelConfT = QtWidgets.QTextEdit(self.widget)
        self.textEditModelConfT.setGeometry(QtCore.QRect(270, 120, 251, 31))
        self.textEditModelConfT.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEditModelConfT.setObjectName("textEditModelConfT")
        self.textEdit_ProcConfT = QtWidgets.QTextEdit(self.widget)
        self.textEdit_ProcConfT.setGeometry(QtCore.QRect(270, 220, 251, 31))
        self.textEdit_ProcConfT.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_ProcConfT.setObjectName("textEdit_ProcConfT")
        self.spinBox_newRam = QtWidgets.QSpinBox(self.widget)
        self.spinBox_newRam.setGeometry(QtCore.QRect(270, 170, 251, 31))
        self.spinBox_newRam.setProperty("value", 16)
        self.spinBox_newRam.setObjectName("spinBox_newRam")

        self.retranslateUi(RegistroConfigTip)
        self.buttonBox.accepted.connect(RegistroConfigTip.accept)
        self.buttonBox.rejected.connect(RegistroConfigTip.reject)
        QtCore.QMetaObject.connectSlotsByName(RegistroConfigTip)

    def retranslateUi(self, RegistroConfigTip):
        _translate = QtCore.QCoreApplication.translate
        RegistroConfigTip.setWindowTitle(_translate("RegistroConfigTip", "Dialog"))
        self.label.setText(_translate("RegistroConfigTip", "CONFIGURACIÓN TIPO"))
        self.label_4.setText(_translate("RegistroConfigTip", "Descripción:"))
        self.label_5.setText(_translate("RegistroConfigTip", "Marca:"))
        self.label_6.setText(_translate("RegistroConfigTip", "Modelo:"))
        self.label_7.setText(_translate("RegistroConfigTip", "Ram:"))
        self.label_8.setText(_translate("RegistroConfigTip", "Procesador:"))
        self.textEdit_DescConfT.setHtml(_translate("RegistroConfigTip", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_MarcConfT.setHtml(_translate("RegistroConfigTip", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEditModelConfT.setHtml(_translate("RegistroConfigTip", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_ProcConfT.setHtml(_translate("RegistroConfigTip", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

import decorativos_rc
