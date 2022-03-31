import pytest

from main import somar_dois_valores, calcular_area_do_circulo


def testar_somar_dois_valores():
    num1 = 8
    num2 = 9
    resultado_esperado = 17

    resultado_atual = somar_dois_valores(num1, num2)
    assert resultado_atual == resultado_esperado


def testar_calcular_area_do_circulo():
    #1 configura
    raio = 1
    resultado_esperado = 3.14

    #2 executa
    resultado_atual = calcular_area_do_circulo(raio)

    #3 valida
    assert resultado_esperado == resultado_atual