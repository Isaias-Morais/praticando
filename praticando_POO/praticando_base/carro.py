class Carro:
    def __init__(self,modelo,velocidade):
        self.modelo = modelo
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 10

    def frear(self):
        if self.velocidade-10 <0:
            self.velocidade=0
        else:
            self.velocidade-=10

carro1 = Carro('Civic',11)
carro1.frear()
carro1.acelerar()
carro1.acelerar()
print(vars(carro1))



