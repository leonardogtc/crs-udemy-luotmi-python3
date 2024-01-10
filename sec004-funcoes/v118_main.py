"""
Exercícios

Crie funções que duplicam, triplicam e quadruplicam o número recebido
como parâmetro.

Pode ser resolvido criando-se funções separadas para executar
o que foi pedido:
"""


# ? def duplicar(numero):
# ?     return numero * 2

# ? def triplicar(numero):
# ?    return numero * 3

# ? def quadruplicar(numero):
# ?    return numero * 4


# Pode-se resolver utilizando técnica de clousure
# Uma função sendo passada para uma variável que se torna
# a propria função já com valor armazenado e adiando a
# entrada de um segundo valor.


def criar_multiplicador(multiplicador):
    """_criar_multiplicador_

    Args:
        multiplicador (_int_): _Número pelo qual se multiplicará os valores_
    """

    def multiplicar(numero):
        return numero * multiplicador

    return multiplicar


# Cria as variáveis/funções
duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

# Cria as saídas determinando o núemro que será multiplicado
print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))
