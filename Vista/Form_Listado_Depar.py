# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form_Listado_Depar.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_Listado_Depar(object):
    def setupUi(self, Form_Listado_Depar):
        Form_Listado_Depar.setObjectName("Form_Listado_Depar")
        Form_Listado_Depar.resize(642, 655)
        self.pushButton_2 = QtWidgets.QPushButton(Form_Listado_Depar)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 600, 121, 51))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(Form_Listado_Depar)
        self.pushButton.setGeometry(QtCore.QRect(320, 600, 131, 51))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form_Listado_Depar)
        self.label.setGeometry(QtCore.QRect(270, 0, 91, 31))
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(Form_Listado_Depar)
        self.widget.setGeometry(QtCore.QRect(0, 30, 631, 561))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(20, 10, 591, 531))
        self.widget_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_2.setObjectName("widget_2")
        self.listWidget_depar = QtWidgets.QListWidget(self.widget_2)
        self.listWidget_depar.setGeometry(QtCore.QRect(10, 20, 571, 511))
        self.listWidget_depar.setObjectName("listWidget_depar")

        self.retranslateUi(Form_Listado_Depar)
        QtCore.QMetaObject.connectSlotsByName(Form_Listado_Depar)

    def retranslateUi(self, Form_Listado_Depar):
        _translate = QtCore.QCoreApplication.translate
        Form_Listado_Depar.setWindowTitle(_translate("Form_Listado_Depar", "Form"))
        self.pushButton_2.setText(_translate("Form_Listado_Depar", "Seleccionar"))
        self.pushButton.setText(_translate("Form_Listado_Depar", "Salir"))
        self.label.setText(_translate("Form_Listado_Depar", "DISPOSITIVOS"))

