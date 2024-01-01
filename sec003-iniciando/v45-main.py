"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""
variavel = 'ABC'

# Imprime a variável sem qualquer alteração de saída
print(f'{variavel}')

# Preenche com espaços vazios à esquerda
print(f'{variavel: >10}')

# Preenche com espaços vazios à esquerda
# O sinal de . foi colocar para podermos
# ver a saída
print(f'{variavel: <10}.')

# Centralizar a saída
print(f'{variavel: ^10}.')
# print(f'{variavel: 0^10}.')

print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')
