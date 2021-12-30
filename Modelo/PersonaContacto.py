class PersonaContacto:
    def __init__(self, nombre):
       self.nombre=nombre

    def __str__(self) -> str:
        return "{} ".format(self.nombre)


