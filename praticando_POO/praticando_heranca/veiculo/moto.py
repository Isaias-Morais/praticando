from praticando_POO.praticando_heranca.veiculo.veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self,marca,modelo,tipo,cor):
        super().__init__(marca,modelo)
        self.tipo = tipo
        self.cor = cor

    def __str__(self):
        return f'{super().__str__()},tipo-{self.tipo},cor-{self.cor}'

    def ligar(self):
        self._ligado = True


