from praticando_POO.Classes_avancadas.O_SistemaDePagamentos.gerente import Gerente
from praticando_POO.Classes_avancadas.O_SistemaDePagamentos.estagiario import Estagiario

fucionarios = []

fucionario1 = Gerente('Isaias',1700)
fucionario2 = Estagiario('Roberto',1700)

fucionarios.append(fucionario1)
fucionarios.append(fucionario2)

for fucionario in fucionarios:
    print(fucionario.CaucularSalario())


