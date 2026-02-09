from praticando_POO.Classes_avancadas.Formas.formas_geometricas import Forma

class Ciculo(Forma):
    def __init__(self,raio):
        self.raio = raio

    def CaucularArea(self):
        return 3.14* self.raio**2

    def CalcularPerimetro(self):
        return (2*3.14*self.raio)