class Conta:
    def __init__(self,numero,titular= '',saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def deposito(self,valor):
        self.saldo += valor

    def sacar(self,valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print('Saldo isuficiente')



conta1  = Conta(12,'isaias',10)
conta1.deposito(1)
conta1.sacar(11)


