from sqlalchemy import create_engine, Integer
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column

#configuracao de conexao
url = "postgresql+psycopg://postgres:postgre@localhost/meu_teste"
engine = create_engine(url)
SessionLocal = sessionmaker(bind=engine)


#Configurando Base

class Base(DeclarativeBase):
    pass

#Criando classe ORM
class Motos(Base):
    __tablename__ = "motos"

    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    marca : Mapped[str] = mapped_column(nullable=False)
    modelo : Mapped[str] = mapped_column(nullable=False)

    def __repr__(self):
        return f'|ID-{self.id}|MARCA-{self.marca}|MODELO-{self.modelo}|'

#Criando tabelas
Base.metadata.create_all(engine)

#adicionando moto

def adicionar_moto(marca=None, modelo=None):
    db = SessionLocal
    moto = Motos(marca=marca,modelo=modelo)
    try:
        db.add(moto)
        db.commit()
    except:
        db.rollback()
        raise
    finally:
        db.close()

#listando motos
def lista_motos():
    db = SessionLocal
    lista = db.query(Motos).all()
    db.close()
    return (lista)

def lista_moto(id):
    db = SessionLocal
    moto = db.query(Motos).filter(Motos.id == id).first()
    db.close()
    return moto

#deletando moto
def deletar_moto(id):
    db = SessionLocal
    try:
        moto = db.query(Motos).filter(Motos.id == id).first()
        if moto:
            db.delete(moto)
            db.commit()
    except:
        db.rollback()
    finally:
        db.close()












