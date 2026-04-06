#pra rodar a api uvicorn praticando_fastAPI.pratica_1:app --reload


from fastapi import FastAPI

#crição do app
app = FastAPI()

#get
@app.get('/')
async def root():
    return {"message": 'Hello World'}

@app.get("/sobre")
async def sobre():
    return {"message": "meu teste em fast api"}


@app.get("/usuario/{nome}")
async def usuario(nome: str):
    return {'message': nome}

@app.get('/busca_produto/{id}')
async def produto(id: int):
    return {'produto_id': id}

@app.get('/busca_pedido/{id}/{status}')
async def pedido(id: int,status: str):
    return {"pedido_id": id,
            "status" : status
            }

@app.get("/pedidos")
async def lista_pedidos():
    return pedidos

@app.get("/pedido/{numero}")
async def pegar_pedido(numero:int):
    if numero >= len(pedidos):
        return {
            'erro':'pedido inexistente'
        }
    return pedidos[numero]


#schermas

from pydantic import BaseModel

class Usuario(BaseModel):
    nome:str
    idade:int


class Produto(BaseModel):
    nome:str
    preco:float

class Pedido(BaseModel):
    produto:str
    quantidade:int

pedidos = []

#post

@app.post("/usuario")
async def criar_usuario(usuario:Usuario):
    return usuario

@app.post('/produto')
async def criar_produto(produto:Produto):
    return produto

@app.post('/pedido')
async def criar_pedido(pedido:Pedido):
    novo_pedido = {
        "produto" : pedido.produto,
        "quantidade" : pedido.quantidade,
        "status" : "Recebido"
    }
    pedidos.append(novo_pedido)

    return novo_pedido


#delete

@app.delete('/pedido/{numero}')
async def deletar_pedido(numero:int):
    if numero >= len(pedidos):
        return {'erro' : 'pedido inexistente'}
    pedidos.pop(numero)
    return {"msg": "pedido removido"}

#put
@app.put("/pedido/{numero}")
async def atualizar_pedido(numero:int,pedido:Pedido):
    if numero < 0 or numero >= len(pedidos):
        return {"erro": "pedido inexistente"}

    pedidos_atualizado = {
        "produto": pedido.produto,
        "quantidade": pedido.quantidade,
        "status": pedidos[numero].get("status","recebido")
    }

    pedidos[numero] = pedidos_atualizado

    return pedidos_atualizado