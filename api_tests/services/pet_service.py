import requests
from api_tests.utils.base import BASE_URL


def criar_pet(payload):

    response = requests.post(
        f"{BASE_URL}/pet",
        json=payload
    )

    return response


def buscar_pet(pet_id):

    response = requests.get(
        f"{BASE_URL}/pet/{pet_id}"
    )

    return response


def atualizar_pet(payload):

    response = requests.put(
        f"{BASE_URL}/pet",
        json=payload
    )

    return response


def deletar_pet(pet_id):

    response = requests.delete(
        f"{BASE_URL}/pet/{pet_id}"
    )

    return response