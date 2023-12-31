# A função input somente é exibida no terminal
nome = input('Qual o seu nome? ')
print(f'O seu nome é {nome}')

# Informação útil
# Mostrar que variável tem determinado valor, basta colocar
# um sinal de igual após a variável, sem espaços
print(f'O seu nome é {nome=}')

# Por padrão uma chamada input retorna um valor de string
numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

# Para se efetuar cálculos deve-se utilizar método de coerção
int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

# print(f'A soma dos números é: {int_numero_1 + int_numero_2}')

# IPC: Pode-se utilizar coerção de variáveis logo na
# entrada dos valores.
# OBS: Segundo instrutor não é uma boa prática de programação python
numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))
print(f"A doma dos valores é: {numero_1 + numero_2}")
