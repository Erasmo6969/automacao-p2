import requests
from api_tests.utils.base import BASE_URL


def criar_pedido(payload):

    response = requests.post(
        f"{BASE_URL}/store/order",
        json=payload
    )

    return response


def buscar_pedido(order_id):

    response = requests.get(
        f"{BASE_URL}/store/order/{order_id}"
    )

    return response


def deletar_pedido(order_id):

    response = requests.delete(
        f"{BASE_URL}/store/order/{order_id}"
    )

    return response