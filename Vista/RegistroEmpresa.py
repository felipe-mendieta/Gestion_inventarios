# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegistroEmpresa.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RegistroEmpresa(object):
    def setupUi(self, RegistroEmpresa):
        RegistroEmpresa.setObjectName("RegistroEmpresa")
        RegistroEmpresa.resize(556, 412)
        RegistroEmpresa.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.buttonBox = QtWidgets.QDialogButtonBox(RegistroEmpresa)
        self.buttonBox.setGeometry(QtCore.QRect(130, 370, 241, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.widget = QtWidgets.QWidget(RegistroEmpresa)
        self.widget.setGeometry(QtCore.QRect(10, 70, 521, 271))
        self.widget.setObjectName("widget")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 211, 41))
        self.label_4.setStyleSheet("font: 12pt \"Sitka Display\";")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(10, 60, 211, 41))
        self.label_6.setStyleSheet("font: 12pt \"Sitka Display\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(10, 120, 211, 41))
        self.label_7.setStyleSheet("font: 12pt \"Sitka Display\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(10, 170, 211, 41))
        self.label_8.setStyleSheet("font: 12pt \"Sitka Display\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(10, 220, 211, 41))
        self.label_9.setStyleSheet("font: 12pt \"Sitka Display\";")
        self.label_9.setObjectName("label_9")
        self.textEdit_NombreEmp = QtWidgets.QTextEdit(self.widget)
        self.textEdit_NombreEmp.setGeometry(QtCore.QRect(270, 20, 251, 31))
        self.textEdit_NombreEmp.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_NombreEmp.setObjectName("textEdit_NombreEmp")
        self.textEdit_DirecEmp = QtWidgets.QTextEdit(self.widget)
        self.textEdit_DirecEmp.setGeometry(QtCore.QRect(270, 70, 251, 31))
        self.textEdit_DirecEmp.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_DirecEmp.setObjectName("textEdit_DirecEmp")
        self.textEdit_TlfnEmp = QtWidgets.QTextEdit(self.widget)
        self.textEdit_TlfnEmp.setGeometry(QtCore.QRect(270, 120, 251, 31))
        self.textEdit_TlfnEmp.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_TlfnEmp.setObjectName("textEdit_TlfnEmp")
        self.textEdit_mailEmp = QtWidgets.QTextEdit(self.widget)
        self.textEdit_mailEmp.setGeometry(QtCore.QRect(270, 170, 251, 31))
        self.textEdit_mailEmp.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_mailEmp.setObjectName("textEdit_mailEmp")
        self.textEdit_PoblEmp = QtWidgets.QTextEdit(self.widget)
        self.textEdit_PoblEmp.setGeometry(QtCore.QRect(270, 220, 251, 31))
        self.textEdit_PoblEmp.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_PoblEmp.setObjectName("textEdit_PoblEmp")
        self.label = QtWidgets.QLabel(RegistroEmpresa)
        self.label.setGeometry(QtCore.QRect(200, 0, 141, 71))
        self.label.setStyleSheet("font: 20pt \"Sitka Display\";")
        self.label.setObjectName("label")

        self.retranslateUi(RegistroEmpresa)
        self.buttonBox.accepted.connect(RegistroEmpresa.accept)
        self.buttonBox.rejected.connect(RegistroEmpresa.reject)
        QtCore.QMetaObject.connectSlotsByName(RegistroEmpresa)

    def retranslateUi(self, RegistroEmpresa):
        _translate = QtCore.QCoreApplication.translate
        RegistroEmpresa.setWindowTitle(_translate("RegistroEmpresa", "Dialog"))
        self.label_4.setText(_translate("RegistroEmpresa", "Nombre:"))
        self.label_6.setText(_translate("RegistroEmpresa", "Dirección:"))
        self.label_7.setText(_translate("RegistroEmpresa", "Teléfono:"))
        self.label_8.setText(_translate("RegistroEmpresa", "Email:"))
        self.label_9.setText(_translate("RegistroEmpresa", "Población:"))
        self.textEdit_NombreEmp.setHtml(_translate("RegistroEmpresa", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_DirecEmp.setHtml(_translate("RegistroEmpresa", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_TlfnEmp.setHtml(_translate("RegistroEmpresa", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_mailEmp.setHtml(_translate("RegistroEmpresa", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_PoblEmp.setHtml(_translate("RegistroEmpresa", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("RegistroEmpresa", "EMPRESA"))

