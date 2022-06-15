import pytest

import requests

base_url = 'https://petstore.swagger.io/v2/user'
headers = {'Content-Type':'aplication/json'}


def testar_criar_usuario():
    # configura
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = "unknown"
    mensagem_esperada = '30'

    # executa
    resposta = requests.post(
        url=base_url,
        data=open('teste/db/user1.json', 'rb'),
        headers=headers

    )

    # Formatação

    corpo_da_resposta = resposta.json()
    print(resposta)
    print(resposta.status_code)
    print(corpo_da_resposta)

    # valida


assert resposta.status_code == status_code_esperado
assert corpo_da_resposta['code'] == codigo_esperado
assert corpo_da_resposta['type'] == tipo_esperado
assert corpo_da_resposta['message'] == mensagem_esperada
