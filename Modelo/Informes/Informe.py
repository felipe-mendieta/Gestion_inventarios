import subprocess
import os
from PyQt5.QtCore import Qt
from Modelo.Ordenador import Ordenador

def cmd(commando):
    subprocess.run(commando, shell=True)
try:
    from fpdf import FPDF
except ImportError:
    cmd("pip install fpdf")
import webbrowser
class Informe():
    def listarDispositivos(self, tipoDeDispositivo):
        pass
    def simple_table(self,nombreColumnas,tipoInforme,data):
        self.data=data
        spacing = 1
        pdf = FPDF()
        pdf.add_page()

        pdf.image('../Vista/Recursos/bannerGif.gif', x=0, y=0, w=210)
        pdf.set_font("Arial", size=12)
        pdf.ln(40)  # move 40 down
        pdf.cell(0, 0, txt=tipoInforme, ln=1, align="C")
        pdf.ln(10)  # move 85 down
        col_width = pdf.w / 2.2
        row_height = 6
        print(self.data)
        for row in self.data:
            for i,item in enumerate(row):

                pdf.cell(col_width, row_height * spacing,
                         txt=nombreColumnas[i], border=1)
                pdf.cell(col_width, row_height * spacing,
                         txt=item, border=1)
                pdf.ln()
            pdf.ln()
        print("Informe de "+tipoInforme)
        pdf.output(r'../Documentos/'+tipoInforme+'.pdf')
        pdf.close()
        #webbrowser.open_new(r'../Documentos/Informe Bajas1.pdf')
        #webbrowser.open_new_tab(r'../Documentos/Informe Bajas1.pdf')

