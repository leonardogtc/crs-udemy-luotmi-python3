# Exercício: Comparar dois valores com entrada INPUT
# Dizer se o valor é maior, menor ou igual ao outro.

# Entrando valores
numero1 = input('Digite o primeiro valor: ')
numero2 = input('Digite o segundo valor: ')

# Executando coerção
num1 = int(numero1)
num2 = int(numero2)

# Efetudando comparação
if num1 > num2:
    print(f"O primeiro valor ({num1}) é maior que o segundo valor ({num2})")
elif num1 < num2:
    print(f"O segundo valor ({num2}) é maior que o primeiro valor ({num1})")
else:
    print(f'O primeiro valor {num1} é igual ao segundo {num2}')
