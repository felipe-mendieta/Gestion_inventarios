from Modelo.Accion import Accion

class CambioDestino(Accion):
    def __init__(self, numSecuencia,fechaAccion,descripcion,nuevaIp,nuevaPrioridad):
        self.nuevaIp=nuevaIp
        self.nuevaPrioridad=nuevaPrioridad
        super().__init__(numSecuencia,fechaAccion,descripcion)
