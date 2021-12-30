import subprocess
import os
from PyQt5.QtCore import Qt

from Contenedores.Contenedores import ContenedorDispositivos, ContenedorDepartamentos
from Modelo.Ordenador import Ordenador
from Informes.Informe import Informe
def cmd(commando):
    subprocess.run(commando, shell=True)
try:
    from fpdf import FPDF
except ImportError:
    cmd("pip install fpdf")
import webbrowser
class InformeFicha(Informe):
    tipoDispo=" "

    def __init__(self,contenedorDispositivos,contenedorDepartamentos):
        self.contenedorDepartamentos=contenedorDepartamentos
        self.contenedorDispositivos=contenedorDispositivos
    def listarDispositivos(self, tipoDeDispositivo):
        datosPc = []
        datosImp = []
        datos=self.contenedorDispositivos.listaDeElementos

        for key,dispos in datos.items():
            if(isinstance(dispos,Ordenador)):

                #self.departamento = departamento
                #self.contacto = contacto
                #self.empresa = empresa

                datosPc.append((key, dispos.marca, dispos.modelo, dispos.numSerie,
                                dispos.procesador, str(dispos.ram),str(dispos.precioCompra),dispos.fechaInstalacion.toString(Qt.ISODate),dispos.fechaFinGarantia.toString(Qt.ISODate),
                                dispos.fechaCompra.toString(Qt.ISODate),dispos.prioridad,dispos.direccionIp,dispos.observaciones))
            else:
                datosImp.append((key, dispos.marca, dispos.modelo, dispos.numSerie,str(dispos.precioCompra),dispos.fechaInstalacion.toString(Qt.ISODate),dispos.fechaFinGarantia.toString(Qt.ISODate),dispos.fechaCompra.toString(Qt.ISODate), dispos.prioridad, dispos.direccionIp,dispos.observaciones))

        if(tipoDeDispositivo.lower()=='computador'):
            self.data=datosPc

            return datosPc
        elif (tipoDeDispositivo.lower()=='impresora'):
            self.data = datosImp
            return datosImp