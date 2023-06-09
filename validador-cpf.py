"""
Foi aperfeiçoado com a ajuda do assistente de IA da OpenAI.
"""


import re
import sys

def calcular_digito_verificador(cpf: str) -> int:
    """
    Calcula o dígito verificador com base nos primeiros nove dígitos do CPF.

    Args:
        cpf (str): CPF sem os dígitos verificadores.

    Returns:
        int: Dígito verificador calculado.
    """
    soma = 0
    contador_regressivo = 10

    for digito in cpf:
        soma += int(digito) * contador_regressivo
        contador_regressivo -= 1

    digito_verificador = (soma * 10) % 11
    return 0 if digito_verificador > 9 else digito_verificador


def validar_cpf(cpf: str) -> bool:
    """
    Verifica se um CPF é válido.

    Args:
        cpf (str): CPF a ser validado.

    Returns:
        bool: True se o CPF é válido, False caso contrário.
    """
    # Remove caracteres não numéricos do CPF
    cpf = re.sub(r'[^0-9]', '', cpf)

    if len(cpf) != 11:
        return False

    # Verifica se todos os dígitos são iguais (CPF sequencial)
    if cpf == cpf[0] * 11:
        return False

    digitos_verificadores = cpf[-2:]
    cpf_base = cpf[:-2]

    # Calcula o primeiro dígito verificador
    digito_verificador_1 = calcular_digito_verificador(cpf_base)
    cpf_base += str(digito_verificador_1)

    # Calcula o segundo dígito verificador
    digito_verificador_2 = calcular_digito_verificador(cpf_base)
    cpf_gerado = cpf_base + str(digito_verificador_2)

    # Verifica se o CPF gerado é igual ao CPF original
    return cpf_gerado[-2:] == digitos_verificadores


# Solicita o CPF ao usuário
entrada = input('CPF [746.824.890-70]: ')

# Remove caracteres não numéricos do CPF fornecido
cpf_enviado_cliente = re.sub(r'[^0-9]', '', entrada)

# Valida o CPF e exibe o resultado
if validar_cpf(cpf_enviado_cliente):
    print(f'{cpf_enviado_cliente} é válido')
else:
    print('CPF inválido')