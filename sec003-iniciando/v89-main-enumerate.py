# Cria a lista de nomes
lista = ['Leonardo', 'Lúcia', 'Oliver']

# Adicionar um nome ao final da lista
lista.append('Ivonete')

# Parte 1 - Utiliza a classe enumerate para gerar uma lista numerada,
# o que quer dizer que é criada um novo elemento numerando os dados
# do conjunto de dados e não referenciando o valor do índice da lista.
# ? lista_enumerada = enumerate(lista)
# ? print(next(lista_enumerada))

# Tanto que pode-se escolher de qual valor a lista iniciará:
# ? lista_enumerada1 = enumerate(lista, start=10)

# O enumerate servirá tanto para uma lista quanto para uma tupla,
# entretanto, para que seja definido logo na criação a quem ser-
# virá, pode-se efetuar a criação já com um tipo específico:
lista_enumerada = list(enumerate(lista))

# Parte 2 - A lista enumerada cria uma lista com índice e valor
# para cada linha mostrada:
# (0, 'Leonardo')
# (1, 'Lúcia')
# ? for item in enumerate(lista):
# ?     print(item)

# Parte 3 - Usa-se o desempacotamento da lista para separar o índice do
# elemento do conjunto.
# ? for item in lista_enumerada1:

# Para contorna o problema da lista sendo consumida pode-se criar a lista
# na própria iteração do FOR:
for item in list(enumerate(lista)):
    # Desempacota os item da lista
    indice, nome = item
    # Imprime o índice e o nome
    print(indice, nome)

# Entretanto, os valores da lista numerada quando consumidos retornam a zero.
# Como o for utilizou os valores agora eles não mais existem:
print('O que existe agora na lista numerada', lista_enumerada)

# * PREFERIDO: Para simplificar pode ser feito assim:
for indice, nome in enumerate(lista):
    print(indice, nome)

# Outra forma:
for tupla_enumerada in enumerate(lista):
    print('FOR DA TUPLA:')
    for valor in tupla_enumerada:
        print(f'\t{valor}')

# Cria um range com os índices da lista, como os índices de uma lista são uma
# sequência numérica, basta que se crie um range de valores numéricos com a
# quantidade de elementos da lista.
# indices = range(len(lista))

# # Mostra os valores
# for indice in indices:
#     print(indice, lista[indice], type(lista[indice]))
