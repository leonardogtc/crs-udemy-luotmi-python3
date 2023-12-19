"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x,y):
    # Definição
    # Mostra somente o resultado: print(x + y)
    # Mostra os argumentos da forma x=1 + y=2: print(f'{x=} + {y=}')
    
    print(f'{x=} + {y=}')

# A chamada de função dessa maneira imprime o resultado
# e o texto None - indicando que a função não retorna
# nada.    
# print(soma(1,2))

# Executando a função - Dessa maneira imprime somente o
# resultado. Os argumentos passados são argumentos posicionais
# que dependem da ordem em que são passados.
soma(1,2)