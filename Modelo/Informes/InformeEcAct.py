import subprocess
import os
from PyQt5.QtCore import Qt, QDate

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
class InformeEcAct(Informe):
    tipoDispo=" "
    data = []

    def __init__(self):
        self.contenedorDepartamentos=ContenedorDepartamentos.getInstance()
        self.contenedorDispositivos=ContenedorDispositivos.getInstance()
    def calucularDepreciacion(self,fechaInstalacion,precio):
        year=365
        diasTrascurridos =fechaInstalacion.daysTo(QDate.currentDate())

        if((diasTrascurridos//year)>=4):
            diasTrascurridos=4*year
        for years in range(diasTrascurridos//year):
            descuento=precio * 0.25;
            precio -= descuento;
        return precio
    def listarDispositivos(self, tipoDeDispositivo):

        lista = []
        datos=self.contenedorDispositivos.listaDeElementos
        for key,dispos in datos.items():
                lista.append((str(dispos.precioCompra),dispos.fechaInstalacion.toString(Qt.ISODate),str(dispos.fechaInstalacion.daysTo(QDate.currentDate())//365),str(self.calucularDepreciacion(dispos.fechaInstalacion,dispos.precioCompra))))
        self.data=lista
        return self.data



