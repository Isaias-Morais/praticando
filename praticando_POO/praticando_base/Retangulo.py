class Retangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def Area(self):
        area = (self.base * self.altura)
        return area

    def Perimetro(self):
        perimetro = (self.base + self.altura) * 2
        return perimetro

retangulo = Retangulo(10,20)
print(retangulo.Perimetro())
print(retangulo.Area())