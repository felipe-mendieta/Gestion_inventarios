import subprocess
from PyQt5.QtCore import Qt, QDate

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
class InformeFinGar(Informe):
    tipoDispo=" "
    data = []

    def __init__(self,contenedorDisp,contenedorContacto,fechaInicio,fechaFin):
        self.fechaFin = fechaFin
        self.fechaInicio=fechaInicio
        self.contenedorContacto=contenedorContacto
        self.contenedorDispositivos=contenedorDisp
    def listarDispositivos(self, tipoDeDispositivo):
        datosPc = []
        datosImp = []
        contactos=self.contenedorContacto.listaDeElementos
        datos=self.contenedorDispositivos.listaDeElementos
        print(datos)
        for key,dispos in datos.items():
            if (self.fechaInicio<=dispos.fechaFinGarantia<=self.fechaFin):
                if(isinstance(dispos,Ordenador)):
                    datosPc.append((key, dispos.marca, dispos.modelo, dispos.numSerie,dispos.departamento,
                                    dispos.procesador, str(dispos.ram), str(contactos[dispos.contacto]),dispos.contacto,
                                    dispos.fechaInstalacion.toString(Qt.ISODate),dispos.fechaFinGarantia.toString(Qt.ISODate)))
                else:
                    datosPc.append((key, dispos.marca, dispos.modelo, dispos.numSerie, dispos.departamento,
                                    str(contactos[dispos.contacto]),dispos.contacto,
                                    dispos.fechaInstalacion.toString(Qt.ISODate),dispos.fechaFinGarantia.toString(Qt.ISODate)))
        if(tipoDeDispositivo.lower()=='computador'):
            self.data=datosPc
            return datosPc
        elif (tipoDeDispositivo.lower()=='impresora'):
            self.data = datosImp
            return datosImp



