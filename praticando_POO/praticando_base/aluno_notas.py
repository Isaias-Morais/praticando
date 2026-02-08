class Aluno:
    def __init__(self,nome,NotasEmLista):
        self.nome = nome
        self.notas = NotasEmLista
        self.media = None

    def caucularMedia(self):
        self.media = sum(self.notas)/len(self.notas)
        return self.media

    def situaçao(self):
        if self.media> 7:
            return "Aprovado"
        elif self.media < 4:
            return "Reprovado"
        else:
            return ('Recuperaçao')

aluno1 = Aluno('isaias',[4,4,4,4])
print(aluno1.caucularMedia())
print(aluno1.situaçao())


