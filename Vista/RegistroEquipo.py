# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegistroEquipo.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RegistroEquipo(object):
    def setupUi(self, RegistroEquipo):
        RegistroEquipo.setObjectName("RegistroEquipo")
        RegistroEquipo.resize(1106, 805)
        RegistroEquipo.setStyleSheet("")
        self.widget_2 = QtWidgets.QWidget(RegistroEquipo)
        self.widget_2.setEnabled(True)
        self.widget_2.setGeometry(QtCore.QRect(20, 60, 641, 521))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.widget_2.setFont(font)
        self.widget_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.widget_2.setAutoFillBackground(False)
        self.widget_2.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.widget_2.setObjectName("widget_2")
        self.label_9 = QtWidgets.QLabel(self.widget_2)
        self.label_9.setGeometry(QtCore.QRect(20, 170, 211, 41))
        self.label_9.setStyleSheet("font: 12pt \"Sitka Display\";")
        self.label_9.setObjectName("label_9")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 211, 41))
        self.label_3.setStyleSheet("font: 12pt \"Sitka Display\";")
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.widget_2)
        self.label_7.setGeometry(QtCore.QRect(20, 120, 211, 41))
        self.label_7.setStyleSheet("font: 12pt \"Sitka Display\";")
        self.label_7.setObjectName("label_7")
        self.label_11 = QtWidgets.QLabel(self.widget_2)
        self.label_11.setGeometry(QtCore.QRect(20, 230, 211, 31))
        self.label_11.setStyleSheet("font: 12pt \"Sitka Display\";")
        self.label_11.setObjectName("label_11")
        self.textEdit_NumSerie = QtWidgets.QTextEdit(self.widget_2)
        self.textEdit_NumSerie.setGeometry(QtCore.QRect(280, 80, 311, 31))
        self.textEdit_NumSerie.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_NumSerie.setObjectName("textEdit_NumSerie")
        self.textEdit_IP = QtWidgets.QTextEdit(self.widget_2)
        self.textEdit_IP.setGeometry(QtCore.QRect(280, 180, 311, 31))
        self.textEdit_IP.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_IP.setObjectName("textEdit_IP")
        self.textEdit_precio = QtWidgets.QTextEdit(self.widget_2)
        self.textEdit_precio.setGeometry(QtCore.QRect(280, 230, 311, 31))
        self.textEdit_precio.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_precio.setObjectName("textEdit_precio")
        self.comboBox_Priorid = QtWidgets.QComboBox(self.widget_2)
        self.comboBox_Priorid.setGeometry(QtCore.QRect(280, 130, 311, 31))
        self.comboBox_Priorid.setObjectName("comboBox_Priorid")
        self.comboBox_Priorid.addItem("")
        self.comboBox_Priorid.addItem("")
        self.comboBox_Priorid.addItem("")
        self.label_13 = QtWidgets.QLabel(self.widget_2)
        self.label_13.setGeometry(QtCore.QRect(20, 20, 211, 41))
        self.label_13.setStyleSheet("font: 12pt \"Sitka Display\";")
        self.label_13.setObjectName("label_13")
        self.comboBox_TipDisp = QtWidgets.QComboBox(self.widget_2)
        self.comboBox_TipDisp.setGeometry(QtCore.QRect(280, 30, 311, 31))
        self.comboBox_TipDisp.setObjectName("comboBox_TipDisp")
        self.comboBox_TipDisp.addItem("")
        self.comboBox_TipDisp.addItem("")
        self.label_32 = QtWidgets.QLabel(self.widget_2)
        self.label_32.setGeometry(QtCore.QRect(20, 280, 211, 31))
        self.label_32.setStyleSheet("font: 12pt \"Sitka Display\";")
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.widget_2)
        self.label_33.setGeometry(QtCore.QRect(20, 320, 211, 41))
        self.label_33.setStyleSheet("font: 12pt \"Sitka Display\";")
        self.label_33.setObjectName("label_33")
        self.textEdit_Marca = QtWidgets.QTextEdit(self.widget_2)
        self.textEdit_Marca.setGeometry(QtCore.QRect(280, 280, 311, 31))
        self.textEdit_Marca.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_Marca.setObjectName("textEdit_Marca")
        self.textEdit_Modelo = QtWidgets.QTextEdit(self.widget_2)
        self.textEdit_Modelo.setGeometry(QtCore.QRect(280, 330, 311, 31))
        self.textEdit_Modelo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_Modelo.setObjectName("textEdit_Modelo")
        self.label_10 = QtWidgets.QLabel(self.widget_2)
        self.label_10.setGeometry(QtCore.QRect(20, 370, 211, 41))
        self.label_10.setStyleSheet("font: 12pt \"Sitka Display\";")
        self.label_10.setObjectName("label_10")
        self.plainTextEdit_observ = QtWidgets.QPlainTextEdit(self.widget_2)
        self.plainTextEdit_observ.setGeometry(QtCore.QRect(280, 380, 311, 141))
        self.plainTextEdit_observ.setPlainText("")
        self.plainTextEdit_observ.setObjectName("plainTextEdit_observ")
        self.pushButton_Guardar = QtWidgets.QPushButton(RegistroEquipo)
        self.pushButton_Guardar.setGeometry(QtCore.QRect(680, 600, 401, 71))
        self.pushButton_Guardar.setStyleSheet("")
        self.pushButton_Guardar.setObjectName("pushButton_Guardar")
        self.widget = QtWidgets.QWidget(RegistroEquipo)
        self.widget.setGeometry(QtCore.QRect(680, 60, 401, 191))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(10, 120, 211, 41))
        self.label_6.setStyleSheet("font: 12pt \"Sitka Display\";")
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 211, 41))
        self.label_5.setStyleSheet("font: 12pt \"Sitka Display\";")
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 211, 41))
        self.label_4.setStyleSheet("font: 12pt \"Sitka Display\";")
        self.label_4.setObjectName("label_4")
        self.dateEdit_FechIns = QtWidgets.QDateEdit(self.widget)
        self.dateEdit_FechIns.setGeometry(QtCore.QRect(220, 30, 110, 22))
        self.dateEdit_FechIns.setObjectName("dateEdit_FechIns")
        self.dateEdit_FechFinGa = QtWidgets.QDateEdit(self.widget)
        self.dateEdit_FechFinGa.setGeometry(QtCore.QRect(220, 80, 110, 22))
        self.dateEdit_FechFinGa.setObjectName("dateEdit_FechFinGa")
        self.dateEdit_FechComp = QtWidgets.QDateEdit(self.widget)
        self.dateEdit_FechComp.setGeometry(QtCore.QRect(220, 130, 110, 22))
        self.dateEdit_FechComp.setObjectName("dateEdit_FechComp")
        self.label_12 = QtWidgets.QLabel(RegistroEquipo)
        self.label_12.setGeometry(QtCore.QRect(380, 0, 331, 61))
        self.label_12.setStyleSheet("font: 12pt \"Sitka Display\";")
        self.label_12.setObjectName("label_12")
        self.pushButton = QtWidgets.QPushButton(RegistroEquipo)
        self.pushButton.setGeometry(QtCore.QRect(680, 680, 401, 71))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.tabWidget_CaracPc = QtWidgets.QTabWidget(RegistroEquipo)
        self.tabWidget_CaracPc.setGeometry(QtCore.QRect(680, 250, 401, 191))
        self.tabWidget_CaracPc.setAutoFillBackground(False)
        self.tabWidget_CaracPc.setObjectName("tabWidget_CaracPc")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textEdit_Procesador = QtWidgets.QTextEdit(self.tab)
        self.textEdit_Procesador.setGeometry(QtCore.QRect(220, 10, 111, 31))
        self.textEdit_Procesador.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_Procesador.setObjectName("textEdit_Procesador")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(10, 10, 211, 41))
        self.label_14.setStyleSheet("font: 12pt \"Sitka Display\";")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(10, 50, 211, 41))
        self.label_15.setStyleSheet("font: 12pt \"Sitka Display\";")
        self.label_15.setObjectName("label_15")
        self.spinBox_Ram = QtWidgets.QSpinBox(self.tab)
        self.spinBox_Ram.setGeometry(QtCore.QRect(220, 60, 111, 31))
        self.spinBox_Ram.setProperty("value", 16)
        self.spinBox_Ram.setObjectName("spinBox_Ram")
        self.comboBox_So = QtWidgets.QComboBox(self.tab)
        self.comboBox_So.setGeometry(QtCore.QRect(220, 110, 111, 31))
        self.comboBox_So.setObjectName("comboBox_So")
        self.label_19 = QtWidgets.QLabel(self.tab)
        self.label_19.setGeometry(QtCore.QRect(10, 100, 171, 41))
        self.label_19.setStyleSheet("font: 12pt \"Sitka Display\";")
        self.label_19.setObjectName("label_19")
        self.tabWidget_CaracPc.addTab(self.tab, "")
        self.widget_3 = QtWidgets.QWidget(RegistroEquipo)
        self.widget_3.setGeometry(QtCore.QRect(20, 590, 641, 191))
        self.widget_3.setAutoFillBackground(False)
        self.widget_3.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.widget_3.setObjectName("widget_3")
        self.label_16 = QtWidgets.QLabel(self.widget_3)
        self.label_16.setGeometry(QtCore.QRect(20, 10, 211, 41))
        self.label_16.setStyleSheet("font: 12pt \"Sitka Display\";")
        self.label_16.setObjectName("label_16")
        self.comboBox_Depar = QtWidgets.QComboBox(self.widget_3)
        self.comboBox_Depar.setGeometry(QtCore.QRect(280, 20, 311, 31))
        self.comboBox_Depar.setObjectName("comboBox_Depar")
        self.comboBox_Empresa = QtWidgets.QComboBox(self.widget_3)
        self.comboBox_Empresa.setGeometry(QtCore.QRect(280, 70, 311, 31))
        self.comboBox_Empresa.setObjectName("comboBox_Empresa")
        self.comboBox_Contacto = QtWidgets.QComboBox(self.widget_3)
        self.comboBox_Contacto.setGeometry(QtCore.QRect(280, 120, 311, 31))
        self.comboBox_Contacto.setObjectName("comboBox_Contacto")
        self.label_17 = QtWidgets.QLabel(self.widget_3)
        self.label_17.setGeometry(QtCore.QRect(20, 60, 211, 41))
        self.label_17.setStyleSheet("font: 12pt \"Sitka Display\";")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.widget_3)
        self.label_18.setGeometry(QtCore.QRect(20, 110, 211, 41))
        self.label_18.setStyleSheet("font: 12pt \"Sitka Display\";")
        self.label_18.setObjectName("label_18")
        self.line = QtWidgets.QFrame(self.widget_3)
        self.line.setGeometry(QtCore.QRect(0, -17, 118, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tabWidget_ConfigTip = QtWidgets.QTabWidget(RegistroEquipo)
        self.tabWidget_ConfigTip.setGeometry(QtCore.QRect(680, 460, 401, 121))
        self.tabWidget_ConfigTip.setAutoFillBackground(False)
        self.tabWidget_ConfigTip.setObjectName("tabWidget_ConfigTip")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_28 = QtWidgets.QLabel(self.tab_4)
        self.label_28.setGeometry(QtCore.QRect(10, 0, 181, 41))
        self.label_28.setStyleSheet("font: 12pt \"Sitka Display\";")
        self.label_28.setObjectName("label_28")
        self.comboBox_ConfigTip = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_ConfigTip.setGeometry(QtCore.QRect(220, 10, 111, 31))
        self.comboBox_ConfigTip.setObjectName("comboBox_ConfigTip")
        self.pushButton_CargarConFt = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_CargarConFt.setGeometry(QtCore.QRect(10, 50, 181, 28))
        self.pushButton_CargarConFt.setObjectName("pushButton_CargarConFt")
        self.tabWidget_ConfigTip.addTab(self.tab_4, "")
        self.label = QtWidgets.QLabel(RegistroEquipo)
        self.label.setGeometry(QtCore.QRect(0, -30, 2371, 1231))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("border-image: url(:/Fondos/Recursos/fondo13.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.actionConfiguracion_Tipo = QtWidgets.QAction(RegistroEquipo)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Iconos/Recursos/iconoActualizar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConfiguracion_Tipo.setIcon(icon)
        self.actionConfiguracion_Tipo.setObjectName("actionConfiguracion_Tipo")
        self.actionRealizar_Accion = QtWidgets.QAction(RegistroEquipo)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Fondos/Recursos/martillo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRealizar_Accion.setIcon(icon1)
        self.actionRealizar_Accion.setObjectName("actionRealizar_Accion")
        self.label.raise_()
        self.widget_2.raise_()
        self.pushButton_Guardar.raise_()
        self.widget.raise_()
        self.label_12.raise_()
        self.pushButton.raise_()
        self.tabWidget_CaracPc.raise_()
        self.widget_3.raise_()
        self.tabWidget_ConfigTip.raise_()

        self.retranslateUi(RegistroEquipo)
        self.tabWidget_CaracPc.setCurrentIndex(0)
        self.tabWidget_ConfigTip.setCurrentIndex(0)
        self.pushButton.clicked.connect(RegistroEquipo.close)
        QtCore.QMetaObject.connectSlotsByName(RegistroEquipo)

    def retranslateUi(self, RegistroEquipo):
        _translate = QtCore.QCoreApplication.translate
        RegistroEquipo.setWindowTitle(_translate("RegistroEquipo", "Form"))
        self.label_9.setText(_translate("RegistroEquipo", "Dirección ip:"))
        self.label_3.setText(_translate("RegistroEquipo", "Numero de Serie:"))
        self.label_7.setText(_translate("RegistroEquipo", "Prioridad:"))
        self.label_11.setText(_translate("RegistroEquipo", "Precio de compra:"))
        self.textEdit_NumSerie.setHtml(_translate("RegistroEquipo", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_IP.setHtml(_translate("RegistroEquipo", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_precio.setHtml(_translate("RegistroEquipo", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.comboBox_Priorid.setItemText(0, _translate("RegistroEquipo", "Alta"))
        self.comboBox_Priorid.setItemText(1, _translate("RegistroEquipo", "Media"))
        self.comboBox_Priorid.setItemText(2, _translate("RegistroEquipo", "Baja"))
        self.label_13.setText(_translate("RegistroEquipo", "Tipo de Dispositivo:"))
        self.comboBox_TipDisp.setItemText(0, _translate("RegistroEquipo", "Computador"))
        self.comboBox_TipDisp.setItemText(1, _translate("RegistroEquipo", "Impresora"))
        self.label_32.setText(_translate("RegistroEquipo", "Marca:"))
        self.label_33.setText(_translate("RegistroEquipo", "Modelo:"))
        self.textEdit_Marca.setHtml(_translate("RegistroEquipo", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_Modelo.setHtml(_translate("RegistroEquipo", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_10.setText(_translate("RegistroEquipo", "Observaciones:"))
        self.pushButton_Guardar.setText(_translate("RegistroEquipo", "GUARDAR"))
        self.label_6.setText(_translate("RegistroEquipo", "Fecha de compra:"))
        self.label_5.setText(_translate("RegistroEquipo", "Fecha fin garantía:"))
        self.label_4.setText(_translate("RegistroEquipo", "Fecha de instalación:"))
        self.label_12.setText(_translate("RegistroEquipo", "INVENTARIOS - CONTROL DE EQUIPOS"))
        self.pushButton.setText(_translate("RegistroEquipo", "SALIR"))
        self.textEdit_Procesador.setHtml(_translate("RegistroEquipo", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_14.setText(_translate("RegistroEquipo", "Procesador:"))
        self.label_15.setText(_translate("RegistroEquipo", "Ram:"))
        self.label_19.setText(_translate("RegistroEquipo", "Sistema Operativo:"))
        self.tabWidget_CaracPc.setTabText(self.tabWidget_CaracPc.indexOf(self.tab), _translate("RegistroEquipo", "Computador"))
        self.label_16.setText(_translate("RegistroEquipo", "Departamento:"))
        self.label_17.setText(_translate("RegistroEquipo", "Empresa"))
        self.label_18.setText(_translate("RegistroEquipo", "Conctacto"))
        self.label_28.setText(_translate("RegistroEquipo", "Configuraciones Tipo:"))
        self.pushButton_CargarConFt.setText(_translate("RegistroEquipo", "Cargar Configuración Tipo"))
        self.tabWidget_ConfigTip.setTabText(self.tabWidget_ConfigTip.indexOf(self.tab_4), _translate("RegistroEquipo", "Configuración Tipo"))
        self.actionConfiguracion_Tipo.setText(_translate("RegistroEquipo", "Configuracion Tipo"))
        self.actionRealizar_Accion.setText(_translate("RegistroEquipo", "Realizar Accion"))

import decorativos_rc