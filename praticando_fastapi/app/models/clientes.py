from pydantic import BaseModel

class Cliente(BaseModel):
    __tablename__ = 'cliente'

    id_ : int
    nome: str
    email : str
    telefone : str

