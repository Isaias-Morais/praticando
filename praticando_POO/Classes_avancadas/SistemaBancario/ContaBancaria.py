from abc import ABC,abstractmethod

class ContaBancaria(ABC):
    def __init__(self,numeroConta, titular,saldo):
        self._numeroConta = numeroConta
        self._titular = titular
        self._saldo = saldo

    def depositarValor(self,valor=0):
        self._saldo += valor

    @abstractmethod
    def sacar(self,valor):
        if self._saldo < valor:
            return False
        else:
            self._saldo -= valor
            return True

