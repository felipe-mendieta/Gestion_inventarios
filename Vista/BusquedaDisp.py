# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BusquedaDisp.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BusquedaDisp(object):
    def setupUi(self, BusquedaDisp):
        BusquedaDisp.setObjectName("BusquedaDisp")
        BusquedaDisp.resize(558, 647)
        BusquedaDisp.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(BusquedaDisp)
        self.label.setGeometry(QtCore.QRect(30, 20, 411, 21))
        self.label.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.listWidget_listDisp = QtWidgets.QListWidget(BusquedaDisp)
        self.listWidget_listDisp.setGeometry(QtCore.QRect(30, 50, 341, 571))
        self.listWidget_listDisp.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.listWidget_listDisp.setObjectName("listWidget_listDisp")
        self.pushButton_editar = QtWidgets.QPushButton(BusquedaDisp)
        self.pushButton_editar.setGeometry(QtCore.QRect(380, 50, 171, 61))
        self.pushButton_editar.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.pushButton_editar.setObjectName("pushButton_editar")
        self.pushButton_borrar = QtWidgets.QPushButton(BusquedaDisp)
        self.pushButton_borrar.setGeometry(QtCore.QRect(380, 110, 171, 61))
        self.pushButton_borrar.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.pushButton_borrar.setObjectName("pushButton_borrar")
        self.pushButton_accion = QtWidgets.QPushButton(BusquedaDisp)
        self.pushButton_accion.setGeometry(QtCore.QRect(380, 170, 171, 71))
        self.pushButton_accion.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.pushButton_accion.setObjectName("pushButton_accion")

        self.retranslateUi(BusquedaDisp)
        QtCore.QMetaObject.connectSlotsByName(BusquedaDisp)

    def retranslateUi(self, BusquedaDisp):
        _translate = QtCore.QCoreApplication.translate
        BusquedaDisp.setWindowTitle(_translate("BusquedaDisp", "Form"))
        self.label.setText(_translate("BusquedaDisp", "Dispositivos:"))
        self.pushButton_editar.setText(_translate("BusquedaDisp", "Editar"))
        self.pushButton_borrar.setText(_translate("BusquedaDisp", "Borrar"))
        self.pushButton_accion.setText(_translate("BusquedaDisp", "Accion"))

import decorativos_rc
