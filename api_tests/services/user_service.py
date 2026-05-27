import requests
from api_tests.utils.base import BASE_URL

def criar_usuario(payload):

    response = requests.post(
        f"{BASE_URL}/user",
        json=payload
    )

    return response


def buscar_usuario(username):

    response = requests.get(
        f"{BASE_URL}/user/{username}"
    )

    return response


def deletar_usuario(username):

    response = requests.delete(
        f"{BASE_URL}/user/{username}"
    )

    return response