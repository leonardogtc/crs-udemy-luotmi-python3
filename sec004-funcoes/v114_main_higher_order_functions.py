"""
Higher Order Functions
Funções de primeira classe
As funções podem ser usadas como variáveis
"""


def saudacao(msg, nome):
    """_saudacao_

    Args:
        msg (_str_): _Uma mensagem_
        nome (_str_): _Um nome_

    Returns:
        _str_: _Retorna uma mensagem texto_
    """
    return f'{msg}, {nome}!'


def executa(funcao, *args):
    """_executa uma função com diversos argumentos_

    Args:
        funcao (_str_): _nome da função que será executada_

    Returns:
        _str_: _mensagem da função do argumento_
    """
    return funcao(*args)


print(
    executa(saudacao, 'Bom dia', 'Luiz')
)
print(
    executa(saudacao, 'Boa noite', 'Maria')
)
