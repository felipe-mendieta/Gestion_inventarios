import glob
import os
import subprocess


def reemplazar_ui(lista):
    nuevaLista=[]
    for nombre in lista:
        nuevaLista.append(nombre.replace(".ui",".py"))
    return nuevaLista

def reemplazar_qrc(lista):
    nuevaLista=[]
    for nombre in lista:
        nuevaLista.append(nombre.replace(".qrc","_rc.py"))
    return nuevaLista


if __name__ == "__main__":
    archivos_ui=glob.glob('*.ui')
    archivos_py=reemplazar_ui(archivos_ui)
    
    recursos_qrc=glob.glob('*.qrc')
    recursos_py=reemplazar_qrc(recursos_qrc)
    
    rutaFicheros=os.getcwd().replace("C:","")

    subprocess.run("cd /", shell=True)
    subprocess.run("cd "+rutaFicheros, shell=True)
    
    for i in range(len(archivos_ui)):
        subprocess.run("pyuic5 -o "+archivos_py[i]+" "+archivos_ui[i], shell=True)

    for i in range(len(recursos_qrc)):
        subprocess.run("pyrcc5 -o "+recursos_py[i]+" "+recursos_qrc[i], shell=True)

