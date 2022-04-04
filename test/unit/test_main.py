import csv

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


def ler_dados_csv():
    dados_csv = [] #criação de uma lista vazia
    nome_arquivo = 'C:/Users/pablo.deryck/PycharmProjects/pythonProject1/test/db/massa_caixa.csv'      #local e nome do arquivo de massa
    try:
        with open(nome_arquivo, newline='') as csvfile:
            campos = csv.reader(csvfile, delimiter = ',')
            next (campos)
            for linha in campos:
                dados_csv.append(linha)
                return dados_csv
    except FileNotFoundError:
        print(f'Arquivo não encontrado: {nome_arquivo}')
    except Exception as fail:
        print(f'Falha imprevista: {fail}')

@pytest.mark.parametrize('id,largura,comprimento,altura,resultado_esperado', ler_dados_csv())
def testar_calcular_volume_do_paralelograma(id, largura, comprimento, altura, resultado_esperado):

    resultado_atual = calcular_volume_do_paralelograma(int(largura), int(comprimento), int(altura))
    assert resultado_atual == int(resultado_esperado)