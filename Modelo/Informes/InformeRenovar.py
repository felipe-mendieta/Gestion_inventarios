import subprocess
from PyQt5.QtCore import Qt, QDate

from Contenedores.Contenedores import ContenedorDispositivos
from Informes.Informe import Informe
from Modelo.Ordenador import Ordenador

def cmd(commando):
    subprocess.run(commando, shell=True)
try:
    from fpdf import FPDF
except ImportError:
    cmd("pip install fpdf")
import webbrowser
class InformeRenovar(Informe):
    tipoDispo=" "
    data = []

    def __init__(self,contenedorDisp,contenedorContac,fechaInicio):
        self.fechaInicio=fechaInicio
        self.contenedorContacto = contenedorContac
        contactos = self.contenedorContacto.listaDeElementos
        self.contenedorDispositivos = contenedorDisp
    def listarDispositivos(self, tipoDeDispositivo):
        datosPc = []
        datosImp = []
        datos=self.contenedorDispositivos.listaDeElementos
        contactos = self.contenedorContacto.listaDeElementos
        print(datos)
        for key,dispos in datos.items():
            if (dispos.fechaInstalacion.daysTo(self.fechaInicio)>0):
                if(isinstance(dispos,Ordenador)):
                    datosPc.append((key, dispos.marca, dispos.modelo, dispos.numSerie,dispos.departamento,
                                    dispos.procesador, str(dispos.ram), str(contactos[dispos.contacto]),dispos.contacto,
                                    dispos.fechaInstalacion.toString(Qt.ISODate)))
                else:
                    datosPc.append((key, dispos.marca, dispos.modelo, dispos.numSerie, dispos.departamento,
                                    str(contactos[dispos.contacto]), dispos.contacto,
                                    dispos.fechaInstalacion.toString(Qt.ISODate)))
        if(tipoDeDispositivo.lower()=='computador'):
            self.data=datosPc
            return datosPc
        elif (tipoDeDispositivo.lower()=='impresora'):
            self.data = datosImp
            return datosImp



