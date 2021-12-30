class ConfiguracionTipo:
    def __init__(self,descripcion,marca,modelo,ram,procesador):
        self.descripcion=descripcion
        self.marca=marca
        self.modelo=modelo
        self.ram=ram
        self.procesador=procesador

    def __str__(self) :
        return "Configuracion tipo de {}".format(self.marca)
        #return "Descripcion: {}\nMarca: {}\nModelo: {}\nRam: {}\nProcesador: {}".format(self.descripcion,self.marca,self.modelo,self.ram,self.procesador)

    def __eq__(self, other) :
        return self.procesador == other.procesador and self.marca == other.marca and self.modelo == other.modelo and self.ram == other.ram and self.procesador == other.procesador

