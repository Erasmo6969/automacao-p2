from api_tests.services.pet_service import (
    criar_pet,
    buscar_pet,
    atualizar_pet,
    deletar_pet
)

payload = {
    "id": 101,
    "name": "rex",
    "status": "available"
}


def test_criar_pet():

    response = criar_pet(payload)

    assert response.status_code == 200


def test_buscar_pet():

    criar_pet(payload)

    response = buscar_pet(101)

    assert response.status_code == 200


def test_atualizar_pet():

    payload_atualizado = {
        "id": 101,
        "name": "rex atualizado",
        "status": "sold"
    }

    response = atualizar_pet(payload_atualizado)

    assert response.status_code == 200


def test_deletar_pet():

    criar_pet(payload)

    response = deletar_pet(101)

    assert response.status_code == 200