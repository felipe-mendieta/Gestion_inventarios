import subprocess
import os
from PyQt5.QtCore import Qt

from Contenedores.Contenedores import ContenedorDispositivos
from Modelo.Ordenador import Ordenador
from Informes.Informe import Informe
def cmd(commando):
    subprocess.run(commando, shell=True)
try:
    from fpdf import FPDF
except ImportError:
    cmd("pip install fpdf")
import webbrowser
class InformeBaja(Informe):
    tipoDispo=" "
    data = []

    def __init__(self,contenedorDisp,fechaInicio,fechaFin):
        self.fechaInicio=fechaInicio
        self.fechaFin=fechaFin
        self.contenedorDispositivos=contenedorDisp
    def listarDispositivos(self, tipoDeDispositivo):
        datosPc = []
        datosImp = []
        datos=self.contenedorDispositivos.listaDeElementos
        for key,dispos in datos.items():
            if (dispos.fechaBaja != None and self.fechaInicio<=dispos.fechaBaja<self.fechaFin):
                if(isinstance(dispos,Ordenador)):
                    datosPc.append((key, dispos.marca, dispos.modelo, dispos.numSerie,
                                    dispos.procesador, str(dispos.ram),
                                    dispos.fechaInstalacion.toString(Qt.ISODate),
                                    str(dispos.precioCompra), dispos.fechaBaja.toString(Qt.ISODate)))
                else:
                    datosImp.append((key, dispos.marca, dispos.modelo, dispos.numSerie,
                                     dispos.fechaInstalacion.toString(Qt.ISODate),
                                     str(dispos.precioCompra), dispos.fechaBaja.toString(Qt.ISODate)))
        if(tipoDeDispositivo.lower()=='computador'):
            self.data=datosPc;
            return datosPc
        elif (tipoDeDispositivo.lower()=='impresora'):
            self.data = datosImp;
            return datosImp
