from praticando_POO.Classes_avancadas.SistemaBancario.ContaBancaria import ContaBancaria


class ContaInvestimetno(ContaBancaria):
    def __init__(self, numero, titular, saldo):
        super().__init__(numero, titular, saldo)

    def sacar(self,valor):
        taxa = valor *0.02
        if self._saldo < (valor+taxa):
            return 'Saldo issuficiente '
        else:
            self._saldo -=(valor+taxa)