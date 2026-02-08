from praticando_POO.praticando_heranca.veiculo.veiculo import Veiculo
class Carro(Veiculo):
    def __init__(self,marca,modelo,portas,cor):
        super().__init__(marca,modelo)
        self.portas = portas
        self.cor = cor

    def __str__(self):
        return f'{super().__str__()},portas-{self.portas},cor-{self.cor}'

    def ligar(self):
        self._ligado = True
