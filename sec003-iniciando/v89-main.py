# Cria a lista de nomes
lista = ['Leonardo', 'Lúcia', 'Oliver']

# Adicionar um nome ao final da lista
lista.append('Ivonete')

# Cria um range com os índices da lista, como os índices de uma lista são uma
# sequência numérica, basta que se crie um range de valores numéricos com a
# quantidade de elementos da lista.
indices = range(len(lista))

# Mostra os valores
for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
