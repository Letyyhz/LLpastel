#Letícia Stefanie Maciel Silva

from fastapi import APIRouter
from domain.schemas.ClienteSchema import ClienteCreate, ClienteUpdate, ClienteResponse

router = APIRouter()

@router.get("/cliente/", tags=["Cliente"])
def get_cliente():
    return {"msg": "cliente get todos executado"}

@router.get("/cliente/{id}", tags=["Cliente"])
def get_cliente_id(id: int):
    return {"msg": "cliente get um executado", "id": id}

@router.post("/cliente/", tags=["Cliente"])
def post_cliente(corpo: ClienteCreate):
    return {
        "msg": "cliente criado",
        "nome": corpo.nome,
        "cpf": corpo.cpf
    }

@router.put("/cliente/{id}", tags=["Cliente"])
def put_cliente(id: int, corpo: ClienteUpdate):
    return {
        "msg": "cliente atualizado",
        "id": id,
        "nome": corpo.nome
    }

@router.delete("/cliente/{id}", tags=["Cliente"])
def delete_cliente(id: int):
    return {"msg": "cliente deletado", "id": id}