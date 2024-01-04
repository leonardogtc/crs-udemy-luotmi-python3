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
#        0   1   2   3
lista = [10, 20, 30, 40]

# insert - Adiciona um item no índice escolhido
lista.insert(0, 5)
print(lista)

# Zera a lista
# lista.clear()

# Ao inserir com um índice maior que a quantidade mas que não existe e está
# fora do range de valores o python colocar o valor no final da lista
# com um índice sequencial ignorando a entrada escolhida para o índice.
lista.insert(100, 5)
print(lista)
print(lista[5])
