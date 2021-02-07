class Persona:
    def __init__(self, nombre, apPaterno, apMaterno):
        self.nombre = nombre
        self._apPaterno = apPaterno
        self.__apMaterno = apMaterno
        
    def metodoPublico(self):
        self.__metodoPrivado()
        
    def __metodoPrivado(self):
        print(self.nombre)
        print(self._apPaterno)
        print(self.__apMaterno)
        
    def setApMaterno(self, apMaterno):
        self.__apMaterno = apMaterno
        
    def getApMaterno(self):
        return self.__apMaterno
        
p1 = Persona("Juan", "Lopez", "Perez")
p1.metodo_publico()

print(p1.nombre)
print(p1._apPaterno)