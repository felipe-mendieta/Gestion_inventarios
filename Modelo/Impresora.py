from Modelo.Dispositivo import Dispositivo
class Impresora(Dispositivo):
    def __init__(self, numSerie, fechaInstalacion, fechaFinGarantia, fechaCompra, prioridad, fechaBaja,
                 direccionIp, observaciones, precioCompra,departamento,contacto,empresa,marca,modelo):
        Dispositivo.__init__(self,numSerie,fechaInstalacion,fechaFinGarantia,fechaCompra,prioridad,fechaBaja,direccionIp,observaciones,precioCompra,departamento,contacto,empresa,marca,modelo)