"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

# Função com argumento *args.
# Pega um número indefinido de valores


def soma(*args):
    print(args, type(args))


soma(1, 2, 3, 4, 5, 6, 7)
