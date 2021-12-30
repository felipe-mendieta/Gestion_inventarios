# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegistroAccion.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RegistroAccion(object):
    def setupUi(self, RegistroAccion):
        RegistroAccion.setObjectName("RegistroAccion")
        RegistroAccion.resize(555, 557)
        self.buttonBox = QtWidgets.QDialogButtonBox(RegistroAccion)
        self.buttonBox.setGeometry(QtCore.QRect(20, 500, 521, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(RegistroAccion)
        self.label.setGeometry(QtCore.QRect(230, 10, 121, 71))
        self.label.setStyleSheet("font: 20pt \"Sitka Display\";")
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(RegistroAccion)
        self.widget.setGeometry(QtCore.QRect(10, 70, 521, 181))
        self.widget.setObjectName("widget")
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setGeometry(QtCore.QRect(10, 10, 211, 41))
        self.label_12.setStyleSheet("font: 12pt \"Sitka Display\";")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setGeometry(QtCore.QRect(10, 60, 211, 41))
        self.label_13.setStyleSheet("font: 12pt \"Sitka Display\";")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.widget)
        self.label_14.setGeometry(QtCore.QRect(10, 110, 211, 41))
        self.label_14.setStyleSheet("font: 12pt \"Sitka Display\";")
        self.label_14.setObjectName("label_14")
        self.textEdit_numSec = QtWidgets.QTextEdit(self.widget)
        self.textEdit_numSec.setGeometry(QtCore.QRect(270, 20, 251, 31))
        self.textEdit_numSec.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_numSec.setObjectName("textEdit_numSec")
        self.textEdit_Desc = QtWidgets.QTextEdit(self.widget)
        self.textEdit_Desc.setGeometry(QtCore.QRect(270, 120, 251, 31))
        self.textEdit_Desc.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_Desc.setObjectName("textEdit_Desc")
        self.dateEdit_Fech = QtWidgets.QDateEdit(self.widget)
        self.dateEdit_Fech.setGeometry(QtCore.QRect(270, 70, 251, 31))
        self.dateEdit_Fech.setObjectName("dateEdit_Fech")
        self.tabWidget_tipAct = QtWidgets.QTabWidget(RegistroAccion)
        self.tabWidget_tipAct.setGeometry(QtCore.QRect(10, 260, 531, 221))
        self.tabWidget_tipAct.setObjectName("tabWidget_tipAct")
        self.tab_cambioDestino_2 = QtWidgets.QWidget()
        self.tab_cambioDestino_2.setObjectName("tab_cambioDestino_2")
        self.label_15 = QtWidgets.QLabel(self.tab_cambioDestino_2)
        self.label_15.setGeometry(QtCore.QRect(0, 10, 211, 41))
        self.label_15.setStyleSheet("font: 12pt \"Sitka Display\";")
        self.label_15.setObjectName("label_15")
        self.textEdit_IPNueva = QtWidgets.QTextEdit(self.tab_cambioDestino_2)
        self.textEdit_IPNueva.setGeometry(QtCore.QRect(270, 20, 251, 31))
        self.textEdit_IPNueva.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_IPNueva.setObjectName("textEdit_IPNueva")
        self.label_16 = QtWidgets.QLabel(self.tab_cambioDestino_2)
        self.label_16.setGeometry(QtCore.QRect(0, 50, 211, 41))
        self.label_16.setStyleSheet("font: 12pt \"Sitka Display\";")
        self.label_16.setObjectName("label_16")
        self.comboBox_nuevaPrio = QtWidgets.QComboBox(self.tab_cambioDestino_2)
        self.comboBox_nuevaPrio.setGeometry(QtCore.QRect(270, 60, 251, 31))
        self.comboBox_nuevaPrio.setObjectName("comboBox_nuevaPrio")
        self.comboBox_nuevaPrio.addItem("")
        self.comboBox_nuevaPrio.addItem("")
        self.comboBox_nuevaPrio.addItem("")
        self.tabWidget_tipAct.addTab(self.tab_cambioDestino_2, "")
        self.tab_ampliacion_2 = QtWidgets.QWidget()
        self.tab_ampliacion_2.setObjectName("tab_ampliacion_2")
        self.label_17 = QtWidgets.QLabel(self.tab_ampliacion_2)
        self.label_17.setGeometry(QtCore.QRect(0, 10, 211, 41))
        self.label_17.setStyleSheet("font: 12pt \"Sitka Display\";")
        self.label_17.setObjectName("label_17")
        self.textEdit_newRam = QtWidgets.QTextEdit(self.tab_ampliacion_2)
        self.textEdit_newRam.setGeometry(QtCore.QRect(260, 20, 251, 31))
        self.textEdit_newRam.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_newRam.setObjectName("textEdit_newRam")
        self.label_18 = QtWidgets.QLabel(self.tab_ampliacion_2)
        self.label_18.setGeometry(QtCore.QRect(0, 50, 211, 41))
        self.label_18.setStyleSheet("font: 12pt \"Sitka Display\";")
        self.label_18.setObjectName("label_18")
        self.textEdit_newProc = QtWidgets.QTextEdit(self.tab_ampliacion_2)
        self.textEdit_newProc.setGeometry(QtCore.QRect(260, 60, 251, 31))
        self.textEdit_newProc.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_newProc.setObjectName("textEdit_newProc")
        self.tabWidget_tipAct.addTab(self.tab_ampliacion_2, "")
        self.tab_baja_2 = QtWidgets.QWidget()
        self.tab_baja_2.setObjectName("tab_baja_2")
        self.label_8 = QtWidgets.QLabel(self.tab_baja_2)
        self.label_8.setGeometry(QtCore.QRect(0, 10, 211, 41))
        self.label_8.setStyleSheet("font: 8pt \"Sitka Display\";")
        self.label_8.setObjectName("label_8")
        self.dateEdit_FechBaj = QtWidgets.QDateEdit(self.tab_baja_2)
        self.dateEdit_FechBaj.setGeometry(QtCore.QRect(220, 20, 110, 22))
        self.dateEdit_FechBaj.setObjectName("dateEdit_FechBaj")
        self.tabWidget_tipAct.addTab(self.tab_baja_2, "")
        self.tab_reparacion_2 = QtWidgets.QWidget()
        self.tab_reparacion_2.setObjectName("tab_reparacion_2")
        self.plainTextEdit_ProblemGar = QtWidgets.QPlainTextEdit(self.tab_reparacion_2)
        self.plainTextEdit_ProblemGar.setGeometry(QtCore.QRect(10, 50, 501, 131))
        self.plainTextEdit_ProblemGar.setObjectName("plainTextEdit_ProblemGar")
        self.label_2 = QtWidgets.QLabel(self.tab_reparacion_2)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 131, 16))
        self.label_2.setObjectName("label_2")
        self.tabWidget_tipAct.addTab(self.tab_reparacion_2, "")

        self.retranslateUi(RegistroAccion)
        self.tabWidget_tipAct.setCurrentIndex(3)
        self.buttonBox.accepted.connect(RegistroAccion.accept)
        self.buttonBox.rejected.connect(RegistroAccion.reject)
        QtCore.QMetaObject.connectSlotsByName(RegistroAccion)

    def retranslateUi(self, RegistroAccion):
        _translate = QtCore.QCoreApplication.translate
        RegistroAccion.setWindowTitle(_translate("RegistroAccion", "Dialog"))
        self.label.setText(_translate("RegistroAccion", "ACCIÓN"))
        self.label_12.setText(_translate("RegistroAccion", "Numero de Secuencia:"))
        self.label_13.setText(_translate("RegistroAccion", "Fecha de Acción:"))
        self.label_14.setText(_translate("RegistroAccion", "Descripción:"))
        self.textEdit_numSec.setHtml(_translate("RegistroAccion", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">123</p></body></html>"))
        self.textEdit_Desc.setHtml(_translate("RegistroAccion", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Accion de cada mes.</p></body></html>"))
        self.label_15.setText(_translate("RegistroAccion", "Dirección ip:"))
        self.textEdit_IPNueva.setHtml(_translate("RegistroAccion", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">192.168.5.2</p></body></html>"))
        self.label_16.setText(_translate("RegistroAccion", "Nueva prioridad:"))
        self.comboBox_nuevaPrio.setItemText(0, _translate("RegistroAccion", "Alta"))
        self.comboBox_nuevaPrio.setItemText(1, _translate("RegistroAccion", "Media"))
        self.comboBox_nuevaPrio.setItemText(2, _translate("RegistroAccion", "Baja"))
        self.tabWidget_tipAct.setTabText(self.tabWidget_tipAct.indexOf(self.tab_cambioDestino_2), _translate("RegistroAccion", "Cambio de Destino"))
        self.label_17.setText(_translate("RegistroAccion", "Nueva Ram:"))
        self.textEdit_newRam.setHtml(_translate("RegistroAccion", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">24</p></body></html>"))
        self.label_18.setText(_translate("RegistroAccion", "Nuevo Procesador:"))
        self.textEdit_newProc.setHtml(_translate("RegistroAccion", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">I9-8422</p></body></html>"))
        self.tabWidget_tipAct.setTabText(self.tabWidget_tipAct.indexOf(self.tab_ampliacion_2), _translate("RegistroAccion", "Ampliacion"))
        self.label_8.setText(_translate("RegistroAccion", "<html><head/><body><p><span style=\" font-size:12pt;\">Fecha Baja:</span></p></body></html>"))
        self.tabWidget_tipAct.setTabText(self.tabWidget_tipAct.indexOf(self.tab_baja_2), _translate("RegistroAccion", "Baja"))
        self.plainTextEdit_ProblemGar.setPlainText(_translate("RegistroAccion", "Falla de Fabrica."))
        self.label_2.setText(_translate("RegistroAccion", "Problema de garantía:"))
        self.tabWidget_tipAct.setTabText(self.tabWidget_tipAct.indexOf(self.tab_reparacion_2), _translate("RegistroAccion", "Reparación"))

