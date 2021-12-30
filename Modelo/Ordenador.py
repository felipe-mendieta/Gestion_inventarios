from Modelo.Dispositivo import Dispositivo


class Ordenador(Dispositivo):
    def __init__(self,numSerie,fechaInstalacion,fechaFinGarantia,fechaCompra,prioridad,fechaBaja,direccionIp,observaciones,precioCompra, procesador,ram,departamento,contacto,empresa,marca,modelo):
        self.procesador=procesador
        self.ram=ram
        Dispositivo.__init__(self,numSerie,fechaInstalacion,fechaFinGarantia,fechaCompra,prioridad,fechaBaja,direccionIp,observaciones,precioCompra,departamento,contacto,empresa,marca,modelo)

    def __str__(self) :

        return super().__str__()+"\nProcesador: "+self.procesador+"\nRam:"+str(self.ram)
