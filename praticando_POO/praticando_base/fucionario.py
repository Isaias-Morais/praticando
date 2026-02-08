class Fucionario:
    def __init__(self,nome,salarioBruto,impostoPorcetagem):
        self.nome = nome
        self.salarioBruto = salarioBruto
        self.imposto = impostoPorcetagem

    def __str__(self):
        return f'{self.nome,self.salarioBruto,self.imposto}'

    def salasrioLiquido(self):
        desconto = self.salarioBruto * (self.imposto/100)
        return self.salarioBruto-desconto

    def aumentarSalario(self,pocetagem):
        aumento = self.salarioBruto * (self.imposto/100)
        self.salarioBruto +=aumento


fucionario1 = Fucionario('Isaias',1500.50,7)

print(fucionario1)
fucionario1.salasrioLiquido()
fucionario1.aumentarSalario(10)
print(fucionario1)
