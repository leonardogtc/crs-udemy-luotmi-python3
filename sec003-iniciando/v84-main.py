"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
# Somente utilizar um sinal de igual com objetos mutáveis
# aponta para o endereço de memória e não gera uma cópia
# dos dados:
lista_1 = ['Leonardo', 'Oliver']
lista_2 = lista_1
lista_1.append('Lúcia')
print(lista_2)

# Esse método cópia os valores da lista como uma nova lista de dados
# como é um objeto mutável, tem que se tomar o cuidado de não apontar
# a informação para um mesmo endereço na memória, portanto, utiliza-se
# o método copy da lista para que não aconteça.
# lista_b = lista_a.copy()
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()
lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)
