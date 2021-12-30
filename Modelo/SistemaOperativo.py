class SistemaOperativo:
    def __init__(self, nombre,version,descripcion):
        self.nombre=nombre
        self.version=version
        self.descripcion=descripcion
    def __str__(self):
        return "{}".format(self.nombre)