from praticando_POO.Classes_avancadas.Formas.formas_geometricas import Forma

class Retangulo(Forma):
    def __init__(self,altura,largura):
        self.altura = altura
        self.largura = largura


    def CaucularArea(self):
        return self.altura * self.largura

    def CalcularPerimetro(self):
        return (self.altura + self.largura) * 2

