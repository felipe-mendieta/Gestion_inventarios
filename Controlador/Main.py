import random
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QAbstractItemView, QAction, QMenu, QActionGroup, QTableWidgetItem, QMessageBox
from Ampliacion import Ampliacion
from Baja import Baja
from CambioDestino import CambioDestino
from Informes.InformeBaja import InformeBaja
from Informes.InformeEcAct import InformeEcAct
from Informes.InformeFicha import InformeFicha
from Informes.InformeFinGar import InformeFinGar
from Informes.InformeRenovar import InformeRenovar
from Modelo.Contenedores.Contenedores import *
from Modelo.Departamento import Departamento
from Modelo.Empresa import Empresa
from Modelo.Impresora import Impresora
from Modelo.Ordenador import Ordenador
from Modelo.PersonaContacto import PersonaContacto
from Modelo.SistemaOperativo import SistemaOperativo
from RealizarInformes import Ui_Form_RealizarInformes
from RegistroAccion import Ui_RegistroAccion
from Reparacion import Reparacion
from VentanaAcercaDe import Ui_AcercaDe
from Vista.BusquedaDisp import Ui_BusquedaDisp
from ConfiguracionTipo import ConfiguracionTipo
from Vista.RegistroConfigTip import Ui_RegistroConfigTip

from Vista.RegistroContacto import Ui_RegistroContacto
from Vista.RegistroDepar import Ui_RegistroDepar
from Vista.RegistroEmpresa import Ui_RegistroEmpresa
from Vista.RegistroEquipo import Ui_RegistroEquipo
from Vista.RegistroSo import Ui_RegistroSo
from Vista.VentanaPrincipal import Ui_WindowsPrincipal
import subprocess

def cmd(commando):
    subprocess.run(commando, shell=True)
try:
    import datetime
except:
    cmd("pip install datetime")

contenedorDisp=ContenedorDispositivos()
contenedorDepar=ContenedorDepartamentos()
contenedorEmpres=ContenedorEmpresas()
contenedorContac=ContenedorContactos()
contenedorSos=ContenedorSos()
contenedorConfTip=ContenedorConfigTip()

def generadorCodigos(anexo=""):
    aleatorios=[str(random.randint(1, 9)) for i in range(4)]
    cod = anexo+''.join(aleatorios)
    return cod
class ventanaAcercaDe(QtWidgets.QMainWindow,Ui_AcercaDe):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

class ventanaDeBusqueda(QtWidgets.QMainWindow, Ui_BusquedaDisp):
    def __init__(self,contenedor):
        QtWidgets.QMainWindow.__init__(self)
        Ui_BusquedaDisp.__init__(self)
        self.setupUi(self)
        self.pushButton_editar.clicked.connect(self.seleccionar)
        self.pushButton_borrar.clicked.connect(self.borrar)
        self.pushButton_accion.clicked.connect(self.ventanaAccion)
        if(isinstance(contenedor,ContenedorDispositivos)):
            self.pushButton_accion.setVisible(True)
        else:
            self.pushButton_accion.setVisible(False)
        self.contenedor=contenedor
        self.cargarDatos()
    def cargarDatos(self):
        self.listWidget_listDisp.clear()
        self.listWidget_listDisp.addItems(self.contenedor.listaDeDatos())
    def actualizarContenedores(self):
        contenedorDisp.guardarDatos()
        contenedorDepar.guardarDatos()
        contenedorConfTip.guardarDatos()
        contenedorContac.guardarDatos()
        contenedorSos.guardarDatos()
        contenedorEmpres.guardarDatos()
    def seleccionar(self):
        try:
            dispSelect = self.listWidget_listDisp.currentItem().text()
        except AttributeError:
            print("No ha seleccionado nada.")
            return
        if(isinstance(self.contenedor,ContenedorDispositivos)):
            self.ventanaEdicion=ventanaRegistroEquip()
            self.ventanaEdicion.textEdit_IP.setEnabled(False)
            self.ventanaEdicion.comboBox_Depar.setEnabled(False)
            self.ventanaEdicion.comboBox_Depar.setEnabled(False)
        elif (isinstance(self.contenedor, ContenedorContactos)):
            self.ventanaEdicion = ventanaRegistroContacto()
        elif (isinstance(self.contenedor, ContenedorEmpresas)):
            self.ventanaEdicion = ventanaRegistroEmpres()
        elif (isinstance(self.contenedor, ContenedorSos)):
            self.ventanaEdicion = ventanaRegistroSo()
        elif (isinstance(self.contenedor, ContenedorDepartamentos)):
            self.ventanaEdicion = ventanaRegistroDepar()
        elif (isinstance(self.contenedor, ContenedorConfigTip)):
            self.ventanaEdicion = ventanaConfiguracionTipo(self)

        self.ventanaEdicion.modoEdicion = True
        elementoAModificar=self.contenedor.listaDeElementos[dispSelect]
        self.ventanaEdicion.cargarDatos(dispSelect,elementoAModificar)
        self.ventanaEdicion.show()
        self.cargarDatos()
        self.actualizarContenedores()
    def borrar(self):
        try:
            dispSelect = self.listWidget_listDisp.currentItem().text()
        except AttributeError:
            print("No ha seleccionado nada.")
            return
        self.ventanaEdicion = ventanaRegistroEquip()
        del self.contenedor.listaDeElementos[dispSelect]
        self.cargarDatos()
        self.actualizarContenedores()
    def ventanaAccion(self):
        try:
            self.ventanaAct=ventanaAcciones(self.listWidget_listDisp.currentItem().text())
            self.ventanaAct.show()
        except:
            print("Sin seleccion")
class ventanaConfiguracionTipo(QtWidgets.QDialog,Ui_RegistroConfigTip):
    """"""
    def __init__(self,ventanaPrincipal):
        QtWidgets.QMainWindow.__init__(self)
        Ui_RegistroConfigTip.__init__(self)
        self.setupUi(self)
        self.buttonBox.clicked.connect(self.guardar)
        self.ventanaPrincipal=ventanaPrincipal
    def guardar(self):
        descripcion=self.textEdit_DescConfT.toPlainText()
        marca=self.textEdit_MarcConfT.toPlainText()
        modelo=self.textEditModelConfT.toPlainText()
        ram=self.spinBox_newRam.text()
        procesador=self.textEdit_ProcConfT.toPlainText()
        configuracionTipo=ConfiguracionTipo(descripcion,marca,modelo,ram,procesador)
        #print(configuracionTipo)
        contenedorConfTip.addConfigTip(generadorCodigos("ConfigTip-"),configuracionTipo)
        print("Configuracion Tipo Guardada.")
        if(self.ventanaPrincipal!=None):
            self.ventanaPrincipal.actualizarConfigTip()
        contenedorConfTip.guardarDatos()
class ventanaRegistroDepar(QtWidgets.QDialog,Ui_RegistroDepar):
    modoEdicion = False
    key = None
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.buttonBox.clicked.connect(self.guardar)
    def guardar(self):
        nombre=self.textEdit_NombreDepar.toPlainText()
        departamento=Departamento(nombre);
        contenedorDepar.addDepartamento(generadorCodigos(nombre[0:3] + "-"),departamento)
        contenedorDepar.guardarDatos()
        print("Departamento guardado.")
    def cargarDatos(self,key,departamento):
        self.textEdit_NombreDepar.setText(departamento)
        self.key = key

class ventanaRegistroSo(QtWidgets.QDialog,Ui_RegistroSo):
    modoEdicion = False
    key = None
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.buttonBox.clicked.connect(self.guardar)
    def guardar(self):
        nombre=self.textEdit_NomSO.toPlainText()
        version=self.textEdit_VersSO.toPlainText()
        descripcion=self.textEdit_DescSO.toPlainText()
        sO=SistemaOperativo(nombre,version,descripcion)
        if(not self.modoEdicion):
            contenedorSos.addEmpresa(generadorCodigos(nombre[0:3] + "-"),sO)
        else:
            contenedorSos.addEmpresa(self.key, sO)
        contenedorSos.guardarDatos()
        print("Sistema Operativo guardado.")
    def cargarDatos(self,key,So):
        self.textEdit_NomSO.setText(So.nombre)
        self.textEdit_DescSO.setText(So.descripcion)
        self.textEdit_VersSO.setText(So.version)
        self.key=key

class ventanaRegistroEmpres(QtWidgets.QDialog,Ui_RegistroEmpresa):
    modoEdicion = False
    key=None
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.buttonBox.clicked.connect(self.guardar)
    def guardar(self):
        nombre=self.textEdit_NombreEmp.toPlainText()
        direccion=self.textEdit_DirecEmp.toPlainText()
        telefono=self.textEdit_TlfnEmp.toPlainText()
        email=self.textEdit_mailEmp.toPlainText()
        poblacion=self.textEdit_PoblEmp.toPlainText()
        empresa=Empresa(nombre,direccion,telefono,email,poblacion)
        if(not self.modoEdicion):
            contenedorEmpres.addEmpresa(generadorCodigos(nombre[0:4]+"-"),empresa)
        else:
            contenedorEmpres.addEmpresa(self.key, empresa)
        contenedorEmpres.guardarDatos()
        print("Empresa guardada.")
    def cargarDatos(self,key,empresa):
        self.key=key
        self.textEdit_NombreEmp.setText(empresa.nombre)
        self.textEdit_DirecEmp.setText(empresa.direccion)
        self.textEdit_TlfnEmp.setText(empresa.telefono)
        self.textEdit_mailEmp.setText(empresa.email)
        self.textEdit_PoblEmp.setText(empresa.poblacion)

class ventanaAcciones(QtWidgets.QDialog,Ui_RegistroAccion):
    modoEdicion = False

    def __init__(self, keyDispositivo):
        QtWidgets.QMainWindow.__init__(self)
        Ui_RegistroAccion.__init__(self)
        self.setupUi(self)
        self.buttonBox.clicked.connect(self.guardar)
        self.keyDispositivo=keyDispositivo
        self.dispositivo=contenedorDisp.listaDeElementos[self.keyDispositivo]
        #print(self.keyDispositivo)
        if(isinstance(self.dispositivo,Impresora)):
            self.tab_ampliacion_2.setEnabled(False)
    def guardar(self):
        numSecuencia=self.textEdit_numSec.toPlainText()
        fechaAccion=datetime.datetime.utcnow()
        descripcion=self.textEdit_Desc.toPlainText()
        tipoDeAccion=self.tabWidget_tipAct.currentIndex()
        #print(self.keyDispositivo)

        if(tipoDeAccion==0):#Cambio de destino
            nuevaIp=self.textEdit_IPNueva.toPlainText()
            nuevaPrioridad=self.comboBox_nuevaPrio.currentText()
            accionDeCambio=CambioDestino(numSecuencia,fechaAccion,descripcion,nuevaIp,nuevaPrioridad)
            self.dispositivo.listaAcciones.append(accionDeCambio)
            self.dispositivo.direccionIp = nuevaIp
            self.dispositivo.prioridad = nuevaPrioridad
        elif(tipoDeAccion==1 and isinstance(self.dispositivo,Ordenador)):# Ampliacion
            nuevaRam=self.textEdit_newRam.toPlainText()
            nuevoProcesador=self.textEdit_newProc.toPlainText()
            accionAmpliacion=Ampliacion( numSecuencia,fechaAccion,descripcion, nuevaRam,nuevoProcesador)
            self.dispositivo.ram=nuevaRam
            self.dispositivo.ram=nuevoProcesador
            self.dispositivo.listaAcciones.append(accionAmpliacion)
        elif (tipoDeAccion == 2):# Baja
            fechaBaja=self.dateEdit_FechBaj.date()
            accionFechaBaja=Baja(numSecuencia,fechaAccion,descripcion, fechaBaja)
            self.dispositivo.listaAcciones.append(accionFechaBaja)
            self.dispositivo.fechaBaja=fechaBaja
        elif (tipoDeAccion == 3):#Reparacion
            problemaDeGarantia=self.plainTextEdit_ProblemGar.toPlainText()
            accionReparacion=Reparacion(numSecuencia,fechaAccion,problemaDeGarantia)
            self.dispositivo.listaAcciones.append(accionReparacion)
        contenedorDisp.guardarDatos()
        print("Acción guardada.")

class ventanaRegistroEquip (QtWidgets.QMainWindow,Ui_RegistroEquipo):
    modoEdicion = False
    key=None
    fechaBaja=None
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.pushButton_Guardar.clicked.connect(self.guardar)
        self.comboBox_TipDisp.currentIndexChanged.connect(self.modoGuardadoDisp)
        self.actionConfiguracion_Tipo.triggered.connect(self.mostrarVentanaConfigTip)
        self.pushButton_CargarConFt.clicked.connect(self.cargarConfigTip)
        self.cargarMenu()
        self.actualizarEmpresas()
        self.actualizarConfigTip()
        self.actualizarContactos()
        self.actializarDepartamentos()
        self.actualizarSos()
    def actualizarSos(self):
        self.comboBox_So.clear()
        self.comboBox_So.addItems(contenedorSos.listaDeDatos())
    def actializarDepartamentos(self):
        self.comboBox_Depar.clear()
        self.comboBox_Depar.addItems(contenedorDepar.listaDeDatos())
    def actualizarEmpresas(self):
        self.comboBox_Empresa.clear()
        self.comboBox_Empresa.addItems(contenedorEmpres.listaDeDatos())
    def actualizarContactos(self):
        self.comboBox_Contacto.clear()
        self.comboBox_Contacto.addItems(contenedorContac.listaDeDatos())
    def actualizarConfigTip(self):
        self.comboBox_ConfigTip.clear()
        self.comboBox_ConfigTip.addItems(contenedorConfTip.listaDeDatos())
    def mostrarVentanaConfigTip(self):
        self.ventCofig=ventanaConfiguracionTipo(self)
        self.ventCofig.show()
        self.actualizarConfigTip()
    def cargarMenu(self):
        mainMenu = self.menuBar()
        configTip = mainMenu.addMenu('Configuracion Tipo')
        configTip.addAction(self.actionConfiguracion_Tipo)
    def modoGuardadoDisp(self):
        if (self.comboBox_TipDisp.currentIndex() == 1):  # Si el dispositivo es una impresora
            self.tabWidget_CaracPc.setEnabled(False)
        elif(self.comboBox_TipDisp.currentIndex() == 0):
            self.tabWidget_CaracPc.setEnabled(True)
    def limpiarDatos(self):
        self.textEdit_Modelo.clear()
        self.textEdit_Marca.clear()
        self.textEdit_IP.clear()
        self.textEdit_Procesador.clear()
        self.textEdit_precio.clear()
        self.textEdit_NumSerie.clear()
        self.plainTextEdit_observ.clear()
        self.dateEdit_FechFinGa.clear()
        self.dateEdit_FechIns.clear()
        self.dateEdit_FechComp.clear()
        self.spinBox_Ram.clear()

    def guardar(self):
        numSerie = self.textEdit_NumSerie.toPlainText()
        direccionIp = self.textEdit_IP.toPlainText()
        observaciones = self.plainTextEdit_observ.toPlainText()
        try:
            precioCompra=float(self.textEdit_precio.toPlainText())
        except:
            print("Ingrese el precio correctamente")
            precioCompra=0
        fechaInstalacion=self.dateEdit_FechIns.date()
        fechaFinGarantia=self.dateEdit_FechFinGa.date()
        fechaCompra=self.dateEdit_FechComp.date()

        prioridad=self.comboBox_Priorid.currentText()
        procesador = self.textEdit_Procesador.toPlainText()
        ram = self.spinBox_Ram.value()  # Es un tipo de dato entero
        departamento=self.comboBox_Depar.currentText()
        contacto=self.comboBox_Contacto.currentText()
        empresa=self.comboBox_Empresa.currentText()

        marca=self.textEdit_Marca.toPlainText()
        modelo=self.textEdit_Modelo.toPlainText()
        if(self.comboBox_TipDisp.currentIndex()==0):#Si el dispositivo es una computadora
            if(not self.modoEdicion):
                numInventario = generadorCodigos("PC" + "-")
            else:
                numInventario=self.key
            dipositivo = Ordenador( numSerie, fechaInstalacion, fechaFinGarantia, fechaCompra,prioridad, self.fechaBaja, direccionIp, observaciones, precioCompra, procesador, ram,departamento,contacto,empresa,marca,modelo)
            print("Computador ")
            #print(dipositivo)
        elif(self.comboBox_TipDisp.currentIndex()==1):
            if (not self.modoEdicion):
                numInventario = generadorCodigos("IMPR" + "-")
            else:
                numInventario=self.key
            dipositivo = Impresora( numSerie, fechaInstalacion, fechaFinGarantia, fechaCompra,prioridad, self.fechaBaja, direccionIp, observaciones, precioCompra,departamento,contacto,empresa,marca,modelo)
            print("Impresora")
            #print(dipositivo)
        contenedorDisp.addDispositivo(numInventario, dipositivo)
        contenedorDisp.guardarDatos()
        print("********Guardado.*********")
        self.limpiarDatos()
    def cargarDatos(self,key,dispositivo):
        self.key=key
        if(isinstance(dispositivo,Ordenador)):
            self.comboBox_TipDisp.setCurrentIndex(0)
        else:
            self.comboBox_TipDisp.setCurrentIndex(1)
        self.textEdit_NumSerie.setText(dispositivo.numSerie)
        self.textEdit_IP.setText(dispositivo.direccionIp)
        self.plainTextEdit_observ.setPlainText(dispositivo.observaciones)
        self.textEdit_precio.setPlainText(str(dispositivo.precioCompra))
        self.textEdit_Marca.setText(dispositivo.marca)
        self.textEdit_Modelo.setText(dispositivo.modelo)

        self.dateEdit_FechIns.setDate(dispositivo.fechaInstalacion)
        self.dateEdit_FechComp.setDate(dispositivo.fechaCompra)
        self.dateEdit_FechFinGa.setDate(dispositivo.fechaFinGarantia)

        self.comboBox_Contacto.setCurrentText(dispositivo.contacto)
        self.comboBox_Depar.setCurrentText(dispositivo.departamento)
        self.comboBox_Empresa.setCurrentText(dispositivo.empresa)
        self.comboBox_Priorid.setCurrentText(dispositivo.prioridad)

        if(isinstance(dispositivo,Ordenador)):
            self.textEdit_Procesador.setText(dispositivo.procesador)
            self.spinBox_Ram.setValue(dispositivo.ram)
            #print("Ram:",dispositivo.ram)
    def cargarConfigTip(self):
        if(len(contenedorConfTip.listaDeElementos)!=0):
            configuracionTipo=contenedorConfTip.listaDeElementos[self.comboBox_ConfigTip.currentText()]
            self.textEdit_Procesador.setText(configuracionTipo.procesador)
            self.spinBox_Ram.setValue(int(configuracionTipo.ram))
            self.plainTextEdit_observ.setPlainText(configuracionTipo.descripcion)
            self.textEdit_Marca.setText(configuracionTipo.marca)
            self.textEdit_Modelo.setText(configuracionTipo.modelo)

class ventanaRegistroContacto(QtWidgets.QDialog,Ui_RegistroContacto):
    modoEdicion = False
    key = None
    telefonoAntiguo = None
    def __init__(self, *args, **kwargs):
        QtWidgets.QDialog.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.buttonBox.clicked.connect(self.guardar)
    def guardar(self):
        nombre=self.textEdit_Nombre.toPlainText()
        contacto=PersonaContacto(nombre)
        telefono=self.textEdit_Telf.toPlainText()

        if(self.modoEdicion):
            contenedorContac.listaDeElementos[telefono] = contenedorContac.listaDeElementos[self.telefonoAntiguo]
            del contenedorContac.listaDeElementos[self.telefonoAntiguo]
            contenedorContac.addContacto(telefono, contacto)
        else:
            contenedorContac.addContacto(telefono, contacto)
        contenedorContac.guardarDatos()
    def cargarDatos(self,key,contacto):
        self.key=key
        self.telefonoAntiguo=key;

        self.textEdit_Nombre.setText(contacto.nombre)
        self.textEdit_Telf.setText(key)

class ventanaInformes(QtWidgets.QMainWindow,Ui_Form_RealizarInformes):
    def __init__(self, *args, **kwargs):
        QtWidgets.QDialog.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.pushButton_MostarDatos.clicked.connect(self.mostrarTabla)
        self.pushButton_limpiar.clicked.connect(self.limpiarTabla)
        self.pushButton.clicked.connect(self.ordenar)
        self.pushButton.setVisible(False)
        self.comboBox_TipoInf.currentIndexChanged.connect(self.ocultarFechas)
    #Referencia:https://github.com/andresnino/PyQt5/blob/master/Tabla%20-%20QTableWidget/tableWidget.py
    def ordenar(self):
        self.tabla.sortItems(4, QtCore.Qt.AscendingOrder)
    def cargarDatos(self,listaDeDatos):
        print(listaDeDatos)
        self.tabla.clearContents()
        row = 0
        columna=0
        for endian in listaDeDatos:#retorna una tupla por cada iteracion
            self.tabla.setRowCount(row + 1)
            while(columna<len(listaDeDatos[0])):
                self.tabla.setItem(row, columna, QTableWidgetItem(endian[columna]))
                columna = columna + 1
            columna = 0
            row += 1

    def ocultarFechas(self):
        self.pushButton.setVisible(False)
        if (self.comboBox_TipoInf.currentIndex() == 0):  # Si es un informe de bajas
            self.dateEdit_Inicio.setEnabled(True)
            self.dateEdit_Fin.setEnabled(True)
        elif (self.comboBox_TipoInf.currentIndex() == 1):
            self.dateEdit_Inicio.setEnabled(True)
            self.dateEdit_Fin.setEnabled(False)
        elif (self.comboBox_TipoInf.currentIndex() == 2):
            self.dateEdit_Inicio.setEnabled(True)
            self.dateEdit_Fin.setEnabled(True)
            self.pushButton.setVisible(True)
        elif (self.comboBox_TipoInf.currentIndex() == 3):
            self.dateEdit_Inicio.setEnabled(False)
            self.dateEdit_Fin.setEnabled(False)
        elif (self.comboBox_TipoInf.currentIndex() == 4):
            self.dateEdit_Inicio.setEnabled(False)
            self.dateEdit_Fin.setEnabled(False)

    def mostrarTabla(self):
        if(self.comboBox_TipoInf.currentIndex()==0):# Si es un informe de bajas

            informe = InformeBaja(contenedorDisp, self.dateEdit_Inicio.date(), self.dateEdit_Fin.date())
            nombreColumnasImpr = (
            "Numero de Inventario", "Marca", "Modelo", "Numero de Serie", "Fecha de Instalacion", "Precio",
            "Fecha de Baja")
            nombreColumnasPc = (
            "Numero de Inventario", "Marca", "Modelo", "Numero de Serie", "Procesador", "Ram", "Fecha de Instalacion",
            "Precio", "Fecha de Baja")
            self.generarInforme(nombreColumnasImpr, nombreColumnasPc, informe, "Dispositivos dados de Baja")

        elif(self.comboBox_TipoInf.currentIndex()==1):
            self.dateEdit_Fin.setVisible(False)
            informe = InformeRenovar(contenedorDisp,contenedorContac, self.dateEdit_Inicio.date())
            nombreColumnasImpr = ( "Numero de Inventario", "Marca", "Modelo", "Numero de Serie", "Departamento", "Persona", "Telefono","Fecha de Instalacion")
            nombreColumnasPc = ("Numero de Inventario", "Marca", "Modelo", "Numero de Serie", "Departamento", "Procesador", "Ram","Persona", "Telefono", "Fecha de Instalacion")
            self.generarInforme(nombreColumnasImpr, nombreColumnasPc, informe, "Dispositivos a Renovar")

        elif(self.comboBox_TipoInf.currentIndex()==2):
            informe = InformeFinGar(contenedorDisp, contenedorContac,self.dateEdit_Inicio.date(), self.dateEdit_Fin.date())
            nombreColumnasImpr = (
            "Numero de Inventario", "Marca", "Modelo", "Numero de Serie", "Departamento", "Persona", "Telefono",
            "Fecha de Instalacion", "Fin de Garantia")
            nombreColumnasPc = ("Numero de Inventario", "Marca", "Modelo", "Numero de Serie", "Departamento", "Procesador", "Ram","Persona", "Telefono", "Fecha de Instalacion", "Fin de Garantia")
            self.generarInforme(nombreColumnasImpr, nombreColumnasPc, informe, "Dispositivos con Fin de Garantia")
            return
        elif(self.comboBox_TipoInf.currentIndex()==3):
            self.dateEdit_Fin.setVisible(False)
            self.dateEdit_Inicio.setVisible(False)
            informe = InformeFicha(contenedorDisp, contenedorDepar)
            nombreColumnasImpr = ("Numero de Inventario", "Marca", "Modelo", "Numero de Serie","Precio", "Fecha de Instalacion", "Fin de Garantia", "Fecha de Compra", "Prioridad","Ip","Observaciones")
            nombreColumnasPc = ("Numero de Inventario", "Marca", "Modelo", "Numero de Serie", "Procesador", "Ram", "Precio","Fecha de Instalacion", "Fin de Garantia", "Fecha de Compra", "Prioridad", "Ip", "Observaciones")
            self.generarInforme(nombreColumnasImpr, nombreColumnasPc, informe, "Ficha de Dispositivos")
            return
        elif(self.comboBox_TipoInf.currentIndex()==4):
            self.dateEdit_Fin.setEnabled(False)
            self.dateEdit_Inicio.setEnabled(False)
            informe = InformeEcAct()
            nombreColumnas = ("Precio", "Fecha de Instalacion", "Años trascurridos", "Valor Actual")
            self.generarInforme(nombreColumnas, nombreColumnas, informe, "Ficha de Economica de Activos")
            return
    def limpiarTabla(self):
        self.tabla.clearContents()
        self.tabla.setRowCount(0)
    def setTamTabla(self,tupla):
        self.tabla.setColumnCount(len(tupla))
        self.tabla.setRowCount(0)

    def generarInforme(self,nombreColumnasImpr,nombreColumnasPc,objetoInforme,nombreInforme):
        if (self.comboBox.currentIndex() == 1):  # si es una impresora
            self.setTamTabla(nombreColumnasImpr)
            self.tabla.setHorizontalHeaderLabels(nombreColumnasImpr)
            if(self.radioButton_GenPdf.isChecked()):
                objetoInforme.simple_table(nombreColumnasImpr, nombreInforme,objetoInforme.listarDispositivos(self.comboBox.currentText()))
                self.label_Estado.setText("PDF GENERADO")
        else:
            self.setTamTabla(nombreColumnasPc)
            self.tabla.setHorizontalHeaderLabels(nombreColumnasPc)
            if (self.radioButton_GenPdf.isChecked()):
                objetoInforme.simple_table(nombreColumnasPc, nombreInforme,objetoInforme.listarDispositivos(self.comboBox.currentText()))
                self.label_Estado.setText("PDF GENERADO")

        self.cargarDatos(objetoInforme.listarDispositivos(self.comboBox.currentText()))


class controlPrincipal(QtWidgets.QMainWindow, Ui_WindowsPrincipal):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.actionRegistrar_Empresa.triggered.connect(self.mostrarVetnanaRegEmpr)
        self.actionRegistrar_Departamento.triggered.connect(self.mostrarVentanaRegDepar)
        self.actionAcerca_De.triggered.connect(self.mostrarVentanaAcerD)
        self.actionRegistrar_Contacto.triggered.connect(self.mostrarVentanaContac)
        self.actionRegistrar_Equipo.triggered.connect(self.mostrarVentanaRegEq)
        self.actionRegistrar_Configuracion_Tipo.triggered.connect(self.mostrarVentanaConfigTip)
        self.actionRegistrar_Sistema_Operativo.triggered.connect(self.mostrarVentanaSo)
        self.actionRealizarInforme.triggered.connect(self.mostrarVentanaInformes)
        self.actionSalir.triggered.connect(self.salir)

        self.actionEditar_Equipo.triggered.connect(self.mostarVentanaBusquedaA)
        self.actionEditar_Contacto.triggered.connect(self.mostarVentanaBusquedaB)
        self.actionEditar_Configuracion_Tipo.triggered.connect(self.mostarVentanaBusquedaC)
        self.actionEditar_Empresa.triggered.connect(self.mostarVentanaBusquedaD)
        self.actionEditar_Departamento.triggered.connect(self.mostarVentanaBusquedaE)
        self.actionEditar_Sistema_Operativo.triggered.connect(self.mostarVentanaBusquedaF)


    def mostarVentanaBusquedaA(self):
        self.vA = ventanaDeBusqueda(contenedorDisp)
        self.vA.label.setText("Dispositivos")
        self.vA.show()
    def mostarVentanaBusquedaB(self):
        self.vB = ventanaDeBusqueda(contenedorContac)
        self.vB.label.setText("Contactos")
        self.vB.show()
    def mostarVentanaBusquedaC(self):
        self.vC = ventanaDeBusqueda(contenedorConfTip)
        self.vC.label.setText("Configuracion Tipo")
        self.vC.show()
    def mostarVentanaBusquedaD(self):
        self.vD = ventanaDeBusqueda(contenedorEmpres)
        self.vD.label.setText("Empresas")
        self.vD.show()
    def mostarVentanaBusquedaE(self):
        self.vE = ventanaDeBusqueda(contenedorDepar)
        self.vE.label.setText("Departamentos")
        self.vE.show()
    def mostarVentanaBusquedaF(self):
        self.vF = ventanaDeBusqueda(contenedorSos)
        self.vF.show()
        self.vF.label.setText("Sistemas Operativos")
    def salir(self):
        self.close()

    def mostrarVentanaInformes(self):
        self.v10=ventanaInformes()
        self.v10.show()
    def mostrarVentanaRegDepar(self):
        self.v9=ventanaRegistroDepar()
        self.v9.show()
    def mostrarVentanaSo(self):
        self.v8 = ventanaRegistroSo()
        self.v8.show()
    def mostrarVentanaConfigTip(self):
        self.v6 = ventanaConfiguracionTipo(None)
        self.v6.show()
    def mostrarVentanaAcerD(self):
        self.v5=ventanaAcercaDe()
        self.v5.show()
    def mostrarVetnanaRegSos(self):
        self.v4 = ventanaRegistroSo()
        self.v4.show()
    def mostrarVetnanaRegEmpr(self):
        self.v3 = ventanaRegistroEmpres()
        self.v3.show()
    def mostrarVentanaContac(self):
        self.v2 = ventanaRegistroContacto()
        self.v2.show()
    def mostrarVentanaRegEq(self):
        self.v1=ventanaRegistroEquip()
        self.v1.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = controlPrincipal()
    window.show()
    app.exec_()