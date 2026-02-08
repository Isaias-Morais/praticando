from praticando_POO.praticando_heranca.banco.banco import Banco

class Agencia(Banco):
    def __init__(self,nome,endereco,numero):
        super().__init__(nome,endereco)
        self.numero = numero 
