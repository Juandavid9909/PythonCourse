class Caja:
    def __init__(self, alto, ancho, largo):
        self.alto = alto
        self.ancho = ancho
        self.largo = largo
        
    def calcularVolumen(self):
        return self.alto * self.ancho * self.largo
    
