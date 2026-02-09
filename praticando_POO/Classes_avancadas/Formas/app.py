from praticando_POO.Classes_avancadas.Formas.Circulo import Ciculo
from praticando_POO.Classes_avancadas.Formas.Retangulo import Retangulo

list = []

item1 = Ciculo(5)
item2 = Retangulo(10,5)

list.append(item1)
list.append(item2)

for item in list:
    print(item.CaucularArea())
    print(item.CalcularPerimetro())


