from abc import ABC, abstractmethod

class Fucionario(ABC):
    def __init__(self,nome='',salario=0):
        self._nome = nome
        self._salario = salario

    @abstractmethod
    def CaucularSalario(self):
        pass

    @property
    def ExibirDados(self):
        return self.nome




