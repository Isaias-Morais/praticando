import sqlite3

#CRIA BANCO DE DADOS SE NAO EXISTIR
conn = sqlite3.connect('HotelPLus.db')
curso = conn.cursor()

#INSERINDO
curso.execute(
    """
        INSERT INTO usuario(nome,email) 
        VALUEs(?,?)
    """,
    ('Isaias morais','isaiasmorasidelima@gmail.com')

)

conn.commit()
