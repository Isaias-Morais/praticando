from praticando_POO.Classes_avancadas.SistemaBancario.ContaBancaria import ContaBancaria

class ContaPoupaca (ContaBancaria):
    def __init__(self,numero,titular,saldo):
        super().__init__(numero,titular,saldo)

    def sacar(self,valor):
        if self._saldo < valor:
            return 'Saldo issuficiente '
        else:
            self._saldo -= valor