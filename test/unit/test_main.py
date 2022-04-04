import pytest

from main import somar_dois_valores, calcular_area_do_circulo, calcular_volume_do_paralelograma


def testar_somar_dois_valores():
    num1 = 8
    num2 = 9
    resultado_esperado = 17

    resultado_atual = somar_dois_valores(num1, num2)
    assert resultado_atual == resultado_esperado

# anotação para utilizar como massa de teste
@pytest.mark.parametrize('raio,resultado_esperado',[
    # valores
     (1, 3.14), #teste 1
     (2, 12.56), #teste 2
     (3, 28.26),# teste 3
     (4, 50.24),
     ('a', 'Falha no calculo, Raio não é um numero'),
 ])
def testar_calcular_area_do_circulo(raio,resultado_esperado):
    #1 configura
   # raio = 1
    # resultado_esperado = 3.14

    #2 executa
    resultado_atual = calcular_area_do_circulo(raio)

    #3 valida
    assert resultado_esperado == resultado_atual

def testar_calcular_volume_do_paralelograma():
    #1 configura

    largura = 5
    comprimento = 10
    altura = 2
    resultado_esperado = 100

    #2 executa
    resultado_atual = calcular_volume_do_paralelograma(largura, comprimento, altura)


    #3 valida

    assert resultado_atual == resultado_esperado