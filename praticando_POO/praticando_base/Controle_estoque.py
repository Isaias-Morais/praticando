class Produto:
    def __init__(self,nome,preco,quantidade):
        self.nome = nome
        self.preco =preco
        self.quantidade = quantidade

    def __str__(self):
        return f'{self.nome:<20}{self.quantidade:<20}{self.preco:<20}'

    def aumentar_quantidade(self,qtd):
        self.quantidade += qtd

    def remover_estoque(self,qtd):
        if self.quantidade-qtd <0:
            print('valor ivalido')
        else:
            self.quantidade -= qtd

    def caucular_valor_total (self):
     return self.preco*self.quantidade



produto1 = Produto("macarrao",3.0,10)
produto1.aumentar_quantidade(10)
produto1.remover_estoque(0)


print(produto1)
print(produto1.caucular_valor_total())


