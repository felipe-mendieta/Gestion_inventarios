class Empresa:
    def __init__(self,nombre,direccion,telefono,email,poblacion):
        self.nombre=nombre
        self.direccion=direccion
        self.telefono=telefono
        self.email=email
        self.poblacion=poblacion

    def __str__(self) :
        return "{}:{}".format(self.nombre,self.telefono)

        
