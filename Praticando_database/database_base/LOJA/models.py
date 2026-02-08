import sqlite3

def conectar_loja():
    conn = sqlite3.connect("loja.db")
    return conn

def cria_tabela():
    conn = conectar_loja()
    curso = conn.cursor()
    curso.execute(
        ''' 
            CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY ,
            nome TEXT,
            preco FLOAT
            )
            
        '''
    )
    conn.commit()
    conn.close()

def adicionar_produto(nome,preço):
    conn = conectar_loja()
    curso = conn.cursor()
    curso.execute(
        '''
            INSERT INTO produtos(nome,preco)
            VALUES (?,?)
        ''',(nome,preço)
    )
    conn.commit()
    conn.close()

def listar_produtos():
    conn = conectar_loja()
    curso = conn.cursor()
    curso.execute(
        '''
            SELECT * FROM produtos
        '''
    )
    lista_de_produtos = curso.fetchall()
    for produtos in lista_de_produtos:
        print(produtos)
    conn.close()
