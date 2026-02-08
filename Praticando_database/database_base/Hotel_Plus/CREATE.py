import sqlite3

#CRIA BANCO DE DADOS SE NAO EXISTIR
conn = sqlite3.connect('HotelPLus.db')
curso = conn.cursor()

curso.execute('''
    CREATE TABLE IF NOT EXISTS usuario(
    id INTEGER PRIMARY KEY,
    nome TEXT,
    email TEXT
    )
'''
)
conn.commit()
conn.close()
