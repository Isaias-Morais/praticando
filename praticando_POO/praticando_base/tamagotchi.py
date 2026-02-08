class Bichinho:
    def __init__(self,nome):
        self.nome = nome
        self.fome = 50
        self.enegia = 50

    def __str__(self):
        return f'{self.nome,self.fome,self.enegia}'

    def comer(self):
        self.enegia += 5
        self.fome -= 10

    def correr(self):
        self.fome += 20
        self.enegia -= 20

    def dormi(self):
        self.fome += 10
        self.enegia += 50

bichinho1 = Bichinho('momo')
print(bichinho1)
bichinho1.comer()
bichinho1.correr()
bichinho1.dormi()
print(bichinho1)