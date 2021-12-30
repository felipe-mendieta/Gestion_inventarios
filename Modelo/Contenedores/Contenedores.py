import os.path as path
try:
    import cPickle as pickle
except ImportError:
    import pickle

class Contenedor:
    def size(self):
        print("No se ha implementado size.")
    def guardarDatos(self):
        print("No se ha implementado guardarDatos.")
    def recuperarDatos(self):
        print("No se ha implementado recuperarDatos.")
    def listaDeDatos(self):
        print("No se ha implementado listarDatos.")
class ContenedorDispositivos(Contenedor):
    listaDeElementos = {}
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if ContenedorDispositivos.__instance == None:
            ContenedorDispositivos()
        return ContenedorDispositivos.__instance
    def __init__(self):
        """ Virtually private constructor. """
        if ContenedorDispositivos.__instance != None:
            raise Exception("No puedes instanciar mas una vez.Esta clase sigue el patron singleton.")
        else:
            ContenedorDispositivos.__instance = self
            self.recuperarDatos()
    def addDispositivo(self,numInventario,Dispositivo):
        self.listaDeElementos[numInventario]=Dispositivo

    def size(self):
        return len(self.listaDeElementos)
    def guardarDatos(self):
        with open('../ArchivosSerializados/dipositivos.dat', 'wb') as f:
            pickle.dump(self.listaDeElementos, f, pickle.HIGHEST_PROTOCOL)
    def recuperarDatos(self):
        if (path.exists('../ArchivosSerializados/dipositivos.dat')):
            with open('../ArchivosSerializados/dipositivos.dat', 'rb') as f:
                self.listaDeElementos = pickle.load(f)
                print(self.listaDeElementos)
        else:
            print("Bienvenido.")

    def listaDeDatos(self):
        return [(str(keyDispo)) for keyDispo in self.listaDeElementos.keys()]



class ContenedorDepartamentos(Contenedor):
    listaDeElementos={}
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if ContenedorDepartamentos.__instance == None:
            ContenedorDepartamentos()
        return ContenedorDepartamentos.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if ContenedorDepartamentos.__instance != None:
            raise Exception("No puedes instanciar mas una vez.Esta clase sigue el patron singleton.")
        else:
            ContenedorDepartamentos.__instance = self
            self.recuperarDatos()
    def addDepartamento(self,codigo,Departamento):
        self.listaDeElementos[codigo]=Departamento
    def size(self):
        return len(self.listaDeElementos)
    def guardarDatos(self):
        with open('../ArchivosSerializados/departamentos.dat', 'wb') as f:
            pickle.dump(self.listaDeElementos, f, pickle.HIGHEST_PROTOCOL)
    def recuperarDatos(self):
        if (path.exists('../ArchivosSerializados/departamentos.dat')):
            with open('../ArchivosSerializados/departamentos.dat', 'rb') as f:
                self.listaDeElementos = pickle.load(f)
                print(self.listaDeElementos)
    def listaDeDatos(self):
        return [(str(key)) for key in self.listaDeElementos.keys()]

class ContenedorEmpresas(Contenedor):
    listaDeElementos={}

    def __init__(self):
        self.recuperarDatos()
    def addEmpresa(self,cif,Empresa):
        self.listaDeElementos[cif]=Empresa
    def size(self):
        return len(self.listaDeElementos)
    def guardarDatos(self):
        with open('../ArchivosSerializados/empresas.dat', 'wb') as f:
            pickle.dump(self.listaDeElementos, f, pickle.HIGHEST_PROTOCOL)
    def recuperarDatos(self):
        if (path.exists('../ArchivosSerializados/empresas.dat')):
            with open('../ArchivosSerializados/empresas.dat', 'rb') as f:
                self.listaDeElementos = pickle.load(f)
                print(self.listaDeElementos)
    def listaDeDatos(self):
        return [(str(key)) for key in self.listaDeElementos.keys()]
class ContenedorSos(Contenedor):
    listaDeElementos= {}

    def __init__(self):
        self.recuperarDatos()
    def addEmpresa(self,codigo, So):
        self.listaDeElementos[codigo]=So
    def size(self):
        return len(self.listaDeElementos)
    def guardarDatos(self):
        with open('../ArchivosSerializados/sistemasOperativos.dat', 'wb') as f:
            pickle.dump(self.listaDeElementos, f, pickle.HIGHEST_PROTOCOL)
    def recuperarDatos(self):
        if (path.exists('../ArchivosSerializados/sistemasOperativos.dat')):
            with open('../ArchivosSerializados/sistemasOperativos.dat', 'rb') as f:
                self.listaDeElementos = pickle.load(f)
                print(self.listaDeElementos)
    def listaDeDatos(self):
        return [(str(key)) for key in self.listaDeElementos.keys()]
class ContenedorContactos(Contenedor):
    listaDeElementos={}
    __instance = None
    @staticmethod
    def getInstance():
        """ Static access method. """
        if ContenedorContactos.__instance == None:
            ContenedorContactos()
        return ContenedorContactos.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if ContenedorContactos.__instance != None:
            raise Exception("No puedes instanciar mas una vez.Esta clase sigue el patron singleton.")
        else:
            ContenedorContactos.__instance = self
            self.recuperarDatos()

    def addContacto(self,telefono, Contacto):
        self.listaDeElementos[telefono]=Contacto

    def size(self):
        return len(self.listaDeElementos)

    def guardarDatos(self):
        with open('../ArchivosSerializados/contactos.dat', 'wb') as f:
            pickle.dump(self.listaDeElementos, f, pickle.HIGHEST_PROTOCOL)

    def recuperarDatos(self):
        if (path.exists('../ArchivosSerializados/contactos.dat')):
            with open('../ArchivosSerializados/contactos.dat', 'rb') as f:
                self.listaDeElementos = pickle.load(f)
                print(self.listaDeElementos)
    def listaDeDatos(self):
        return [(str(key)) for key,valor in self.listaDeElementos.items()]
class ContenedorConfigTip(Contenedor):
    listaDeElementos={}

    def __init__(self):
        self.recuperarDatos()
    def addConfigTip(self,key,configuracionTipo):
        self.listaDeElementos[key] = configuracionTipo

    def size(self):
        return len(self.listaDeElementos)
    def guardarDatos(self):
        with open('../ArchivosSerializados/configuracionesTipo.dat', 'wb') as f:
            pickle.dump(self.listaDeElementos, f, pickle.HIGHEST_PROTOCOL)

    def recuperarDatos(self):
        if (path.exists('../ArchivosSerializados/configuracionesTipo.dat')):
            with open('../ArchivosSerializados/configuracionesTipo.dat', 'rb') as f:
                self.listaDeElementos = pickle.load(f)
                print(self.listaDeElementos)
    def listaDeDatos(self):
        return [(str(configTip)) for configTip in self.listaDeElementos]