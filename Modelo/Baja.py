from Modelo.Accion import Accion
class Baja(Accion):
    def __init__(self,numSecuencia,fechaAccion,descripcion, fechaBaja):
        self.fechaBaja=fechaBaja
        super().__init__(numSecuencia,fechaAccion,descripcion)
