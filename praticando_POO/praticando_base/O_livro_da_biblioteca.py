class Livro:
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def __str__(self):
        return f'{self.titulo},{self.autor},{self.disponivel} '

    def emprestar(self):
        if self.disponivel == True:
            self.disponivel = False
        else:
            return ('Indisponivel')

    def devolver(self):
        self.disponivel = True


livro1 = Livro('lock','marvel')
livro1.emprestar()
livro1.devolver()
livro1.emprestar()
print(livro1)

