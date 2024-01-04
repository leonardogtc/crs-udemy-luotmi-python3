"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

# Concatenar as lista para uma nova lista,
# deixando as listas originais intactas.
lista_c = lista_a + lista_b
print(lista_c)

# Estendendo a listas a - esse método aumenta o número de
# elementos da lista_a com os elementos existentes na lista_b
# posicionando-os ao final da lista de elementos na lista_a.
lista_a.extend(lista_b)
print(lista_a)
