class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
Persona.nombre = "Juan"
Persona.edad = 28

print(Persona.nombre)

persona = Persona("Karla", 30)

persona2 = Persona("Carlos", 40)