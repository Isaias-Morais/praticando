from fastapi import APIRouter
from praticando_fastapi.app.models.clientes import Cliente

router = APIRouter(
    prefix='/cliente'
)

@router.get('/')
async def listar_clientes():

    clientes_list = [Cliente(nome='isaias',email='isaias@gmail.com',telefone='82981799887'),
                     Cliente(nome='morais',email='morais@gmail.com',telefone='82981799887')]
    return clientes_list