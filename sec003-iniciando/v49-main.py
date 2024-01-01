"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

# Estourando uma exceção
# print(1234)
# print(5678)

# ValueError: invalid literal for int() with base 10: 'a'
# int('a')

numero_str = input(
    'Vou dobrar o número que vc digitar: '
)

# Nota: O método isdigit() verifica se o que foi digitado
# pelo usuário foram somente números. Entretanto, se usar
# o if para fazer a verificação haverá o retorno da instrução
# print('Isso não é um número')
# -----------------------------------------------------------
# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')
# -----------------------------------------------------------

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')
