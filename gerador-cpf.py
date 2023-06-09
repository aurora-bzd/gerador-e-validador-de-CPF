import re
import sys
import random


def gerar_cpf():
    """
    Função que gera um CPF aleatório.
    """
    cpf_base = ''
    for _ in range(9):
        cpf_base += str(random.randint(0, 9))

    digito_verificador_1 = calcular_digito_verificador(cpf_base)
    digito_verificador_2 = calcular_digito_verificador(cpf_base + str(digito_verificador_1))

    cpf_gerado = cpf_base + str(digito_verificador_1) + str(digito_verificador_2)
    return cpf_gerado


def calcular_digito_verificador(cpf_base):
    """
    Função que calcula um dígito verificador para um CPF base dado.
    """
    soma = 0
    contador = len(cpf_base) + 1

    for digito in cpf_base:
        soma += int(digito) * contador
        contador -= 1

    digito_verificador = (soma * 10) % 11
    digito_verificador = digito_verificador if digito_verificador <= 9 else 0

    return digito_verificador


# Exemplo de uso:
cpf_gerado = gerar_cpf()
print(cpf_gerado)
