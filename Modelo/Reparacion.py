from Modelo.Accion import Accion
class Reparacion(Accion):
    def __init__(self,numSecuencia,fechaAccion,descripcion):
        super().__init__(numSecuencia,fechaAccion,descripcion)
    