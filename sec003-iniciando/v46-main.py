"""
Fatiamento de strings
012345678
Olá mundo
# The line `-987654321` is not doing anything in the code.
# It appears to be a comment or a placeholder
# that has no effect on the execution of the code.
-987654321
Fatiamento [i:f:p] [::]
# i - início f - fim p - passos
# (de quantos em quantos caracteres irá pular)
Obs.: a função len retorna a qtd de caracteres da str
"""
var = 'Olá mundo'

# A contagem é diferente da posição dos índices
# Retornará 9 caracteres
print(len(var))

# Capturar uma única posição de índice
# Índices iniciam em zero
# Retornará 'á' - Pos: 012345678
print(var[2])

# Retornar uma sequencia de caracteres
# De uma posição iniciar a uma posição final
# O caractere da posição final é suprimido (padrão do python)
#  0  1  2  3  4  5  6  7  8
#  O  l  á     m  u  n  d  o
# -9 -8 -7 -6 -5 -4 -3 -2 -1
# Começando o 1 indo até o 4 seria: lá m
# Entretanto a saída será: lá
print(var[1:4])

# Mostrando do início até x posições
print(var[:4])

# Escolhendo uma posição inicial e fatiando até o final
print(var[4:])

# Usando índices negativos
#  0  1  2  3  4  5  6  7  8
#  O  l  á     m  u  n  d  o
# -9 -8 -7 -6 -5 -4 -3 -2 -1
print(var[-5: -1])
print(var[-5:])

# O espaço é contado e posicionado como índice
print(len(var[3]))

# usando passos
print(var[0:len(var):1])
print(var[0:len(var):2])
print(var[0:len(var):3])

# Inverter a string com passos
print(var[::-1])
