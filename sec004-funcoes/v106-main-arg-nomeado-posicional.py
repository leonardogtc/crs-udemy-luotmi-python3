"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""


# ? def soma(x, y):
def soma(x, y, z):
    # Definição
    # Mostra somente o resultado: print(x + y)
    # Mostra os argumentos da forma x=1 + y=2: print(f'{x=} + {y=}')

    # ? print(f'{x=} + {y=}')
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)

# A chamada de função dessa maneira imprime o resultado
# e o texto None - indicando que a função não retorna
# nada.
# print(soma(1,2))


# Executando a função - Dessa maneira imprime somente o
# resultado. Os argumentos passados são argumentos posicionais
# que dependem da ordem em que são passados.
# ? soma(1, 2)
soma(1, 2, 3)

# Argumento nomeado posicional - Não preciso me preocupar com
# a ordem caso indique que parâmetro nomeado receberá o valor.
# Toda vez que nomear um argumento tem que nomear todos os
# subsequentes: soma(1, y=2, z=3)
# ? soma(y=2, x=1)

soma(y=2, z=3, x=1)
