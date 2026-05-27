from api_tests.services.user_service import (
    criar_usuario,
    buscar_usuario,
    deletar_usuario
)

payload = {
    "id": 1,
    "username": "erasmo",
    "firstName": "Erasmo",
    "lastName": "Alves",
    "email": "erasmo@email.com",
    "password": "123456",
    "phone": "99999999",
    "userStatus": 1
}


def test_criar_usuario():

    response = criar_usuario(payload)

    assert response.status_code == 200


def test_buscar_usuario():

    criar_usuario(payload)

    response = buscar_usuario("erasmo")

    assert response.status_code == 200


def test_deletar_usuario():

    criar_usuario(payload)

    response = deletar_usuario("erasmo")

    assert response.status_code == 200