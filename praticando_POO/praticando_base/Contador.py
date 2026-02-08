class Contador:
    def __init__(self,valor=0):
        self.valor = valor

    def icrementar(self):
        self.valor += 1

    def reduzir(self):
        self.valor -= 1

    def zerar(self):
        self.valor = 0

    def retorna_valor(self):
        return f"{self.valor}"


valor = Contador(3)
valor.zerar()
valor.icrementar()
valor.reduzir()
print(valor.retorna_valor())


