from Modelo.Accion import Accion
class Ampliacion(Accion):
    
    def __init__(self, numSecuencia,fechaAccion,descripcion, nuevaRam,nuevoProcesador):
        self.nuevaRam=nuevaRam
        self.nuevoProcesador=nuevoProcesador
        super().__init__(numSecuencia,fechaAccion,descripcion)