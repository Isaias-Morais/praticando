from sqlalchemy import create_engine, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker,DeclarativeBase,Mapped, mapped_column, relationship

#me conectando ao banco de dados e criando sessao
url = "postgresql+psycopg://postgres:postgre@localhost/meu_teste"
engine = create_engine(url)
SessionLocal = sessionmaker(bind=engine)

#clase base
class Base(DeclarativeBase):
    pass

#classe motoboy
class Motoboy(Base):
    __tablename__ = "motoboy"

    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    nome : Mapped[str] = mapped_column(nullable=False)
    idade : Mapped[int] = mapped_column(nullable=False)

    #relaçao um motoboy tem muitas motos
    motos = relationship('motos', back_populates='motoboy')

    #apresentacao motoboy
    def __repr__(self):
        return f"|ID-{self.id}|NOME-{self.nome}|IDADE-{self.idade}|"

#classe moto
class Motos(Base):
    __tablename__ = "motos"
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    marca : Mapped[str] = mapped_column(nullable=False)
    modelo : Mapped[str] = mapped_column(nullable=False)

    # chave estrangeira de conexao com motoboy
    motoboy_id : Mapped[int] = mapped_column(Integer,ForeignKey('motoboy.id'))

    #ralacao revesar : motos pertence a um motoboy
    motoboy = relationship('Pai', back_populates='motos')

    def __repr__(self):
        return f'|ID-{self.id}|MARCA-{self.marca}|MODELO-{self.modelo}|'

# criando tabelas
Base.metadata.create_all(engine)


