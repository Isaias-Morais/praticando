from praticando_POO.Classes_avancadas.O_SistemaDePagamentos.fucionario import Fucionario

class Gerente(Fucionario):
    def __init__(self,nome,salario):
        super().__init__(nome,salario)
        self.porcetagem = 20

    def CaucularSalario(self):
        extra = (self._salario*20)/100
        return self._salario + extra





