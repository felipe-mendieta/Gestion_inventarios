class Dispositivo:
    listaAcciones=[]

    def __init__(self,numSerie,fechaInstalacion,fechaFinGarantia,fechaCompra,prioridad,fechaBaja,direccionIp,observaciones,precioCompra,departamento,contacto,empresa,marca,modelo):
        self.numSerie=numSerie
        self.fechaInstalacion=fechaInstalacion
        self.fechaFinGarantia=fechaFinGarantia
        self.fechaCompra=fechaCompra
        self.prioridad=prioridad
        self.fechaBaja=fechaBaja
        self.direccionIp=direccionIp
        self.observaciones=observaciones
        self.precioCompra=precioCompra
        self.departamento=departamento
        self.contacto=contacto
        self.empresa=empresa
        self.marca=marca
        self.modelo=modelo
    def addAccion(self,Accion):
        self.listaAcciones.append(Accion)
    def __str__(self) :
        return "Numero de Serie:{}\nFecha Instalacion:{}\nFin de Garantia: {}\nFecha Compra: {}\nFecha de Baja: {} \nIp: {}\nObservaciones:{}\nPrecioCompra:{}\nPrioridad:{}\nMarca:{}\nModelo:{}".format(self.numSerie,self.fechaInstalacion,self.fechaFinGarantia,self.fechaCompra,self.fechaBaja,self.direccionIp,self.observaciones,self.precioCompra,self.prioridad,self.marca,self.modelo)
