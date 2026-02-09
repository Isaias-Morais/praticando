from praticando_POO.Classes_avancadas.SistemaBancario.ContaBancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def __init__(self,numero,titular,saldo):
        super().__init__(numero,titular,saldo)


    def sacar(self,valor):
        taxa = 0.5
        if self._saldo < (valor+taxa):
            return 'Saldo issuficiente '
        else:
            self._saldo -=(valor+taxa)




