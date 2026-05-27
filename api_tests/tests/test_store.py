from api_tests.services.store_service import (
    criar_pedido,
    buscar_pedido,
    deletar_pedido
)

payload = {
    "id": 500,
    "petId": 101,
    "quantity": 1,
    "shipDate": "2026-05-27T10:00:00.000Z",
    "status": "placed",
    "complete": True
}


def test_criar_pedido():

    response = criar_pedido(payload)

    assert response.status_code == 200


def test_buscar_pedido():

    criar_pedido(payload)

    response = buscar_pedido(500)

    assert response.status_code == 200


def test_deletar_pedido():

    criar_pedido(payload)

    response = deletar_pedido(500)

    assert response.status_code == 200