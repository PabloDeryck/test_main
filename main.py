import pytest

def somar_dois_valores(num1, num2):
    return num1 + num2


def subtrai_dois_valores(num1, num2):
    return num1 - num2

def multiplica_dois_valores(num1, num2):
    return num1 * num2


def divisao_dois_valores(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return 'Não é possivel dividir por 0'

def elevar_um_numero_pelo_outro(num1, num2):
    return num1 ** num2

#calcular e testar a area de um circulo
# area = pi * raio ** 2

def calcular_area_do_circulo(raio):
    return  3.14 * raio ** 2


if __name__ == '__main__':
    resultado = somar_dois_valores(7, 9)
    print(f'Valor da soma {resultado}')

    resultado = subtrai_dois_valores(47, 15)
    print(f'Valor da subtracao {resultado}')

    resultado = multiplica_dois_valores(47, 15)
    print(f'Valor da multiplicacao {resultado}')

    resultado = divisao_dois_valores(478, 12)
    print(f'Valor da divisao {resultado}')

    resultado =elevar_um_numero_pelo_outro(2, 3)
    print(f'Valor da potenciaçao {resultado}')
