"""
Introdução ao empacotamento e desempacotamento + tuplas
"""

# Parte 1 da explicação
# ? nomes = ['Leonardo', 'Lúcia', 'Oliver']
# ? nome1, nome2, nome3 = nomes
# ? print(nome2)

# Parte 2 - simplificando
# ? nome1, nome2, nome3 = ['Leonardo', 'Lúcia', 'Oliver']

# Parte 3 - Caso não tenha variáveis suficientes para
# receber os valores, vai gerar um erro com a seguinte
# descrição:
# ValueError: too many values to unpack
# ? nome1, nome2 = ['Leonardo', 'Lúcia', 'Oliver']

# Parte 4 - Caso haja mais variáveis que valores,
# vai gerar um erro com a seguinte descrição:
# ValueError: not enough values to unpack
# ? nome1, nome2, nome3, nome4 = ['Leonardo', 'Lúcia', 'Oliver']
# ? print(nome2)

# Parte 5 - Empacotando o restante dos valores. Para tal basta
# colocar uma variável qualquer com um sinal de '*' no ínicio
# à esquerda: *resto, *restante, *xx (qualquer nome)
# ? nome1, *resto = ['Leonardo', 'Lúcia', 'Oliver']
# ? print(nome1, resto)

# Quando se precisa de uma variável mas não predente-se usá-la no sistema
# por convenção dos programadores em Python utiliza-se o sinal de '_".
# ? nome1, *_ = ['Leonardo', 'Lúcia', 'Oliver']
# ? print(nome1, _)

# Ignora os dois primeiros valores e pega somente o terceiro
# gerando um *resto com uma lista vazia já que não existe mais
# nada a partir do terceiro valor ou segundo índice da lista.
_, _, nome, *resto = ['Leonardo', 'Lúcia', 'Oliver']
print(nome)
