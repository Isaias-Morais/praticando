from praticando_POO.Classes_avancadas.O_SistemaDePagamentos.fucionario import Fucionario

class Estagiario(Fucionario):
    def __init__(self,nome, salario):
        super().__init__(nome,salario)
        self._ValeTransporte = 100

    def CaucularSalario(self):
        return self._salario + self._ValeTransporte
