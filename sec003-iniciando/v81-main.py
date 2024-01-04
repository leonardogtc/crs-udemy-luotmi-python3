"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
# Uma lista de valores pode suportar valores de qualquer tipo.
# para criar uma lista basta associar os dessa forma: lista = [10, 20, 30, 40]
# Uma lista é posicionada por índices começando por zero
#         0   1   2   3
lista = [10, 20, 30, 40]

# Exibir o conteúdo da lista
print(lista)

# Para exibir o conteúdo de um índice: print(lista[2])
print('Índice 2: ', lista[2])

# Pegar um valor da lista para uma variável
numero = lista[2]
print(numero)

# Uma lista é um objeto mutável, os valores podem ser alterados
lista[2] = 300
print(lista)
print('Índice 2: ', lista[2])
numero = lista[2]
print(numero)

# Deletar uma valor da lista
del lista[2]
print(lista)
print('Índice 2: ', lista[2])

# Acrescentar itens ao final da lista
lista[2] = 30
lista.append(40)
lista.append(50)
lista.append(60)
print(lista)

# Remover o último elemento de uma listas
lista.pop()
print(lista)

# O pop retorna o último valor removido
# que pode ser armazenado em uma variável
# ultimo_valor = lista.pop()

# O pop pode apagar um valor específico pelo índice
ultimo_valor = lista.pop(3)
print(lista, 'Removido,', ultimo_valor)
