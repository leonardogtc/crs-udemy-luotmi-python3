"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len)
# A string pode ser acessada como uma lista entretanto
# é uma listas imutável. Somente direcionando para outra
# variável como foi visto antes
lista = []    # Lista vazia

# Uma lista vazia em boolean retorna False
print(bool([]))

# Uma lista tem seu próprio tipo - Uma classe list
print(lista, type(lista))

# Uma lista suporta vários valores de qualquer tipo
# inclusive uma lista interna como elemento.
#        0    1      2              3    4
#       -5   -4     -3             -2   -1
lista = [123, True, 'Luiz Otávio',  1.2, []]
print(lista)

# Uma lista pode ser modificada e pode ser acessada
# por índices negativos, começando do -1 à direita
# como mostrado abaixo:
lista[-3] = 'Maria'
print(lista)

# A lista comporta diversos tipos e um índice comporta
# elementos completos, por exemplo, o nome é uma string
# que não pode ser separada em índices
print(lista[2], type(lista[2]))
