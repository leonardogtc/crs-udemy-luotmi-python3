"""
    Manipulando chaves e valores em dicionários
"""

# Em alguns casos, mypy não consegue inferir o tipo de uma variável sem uma
# anotação explícita. Mypy trata isso como um erro. Isso normalmente acontece
# quando você inicializa uma variável com uma coleção vazia ou None. Se mypy
# não puder inferir o tipo de item da coleção, mypy substituirá quaisquer
# partes do tipo que não pôde inferir por Any e gerará um erro.
pessoa = {}

# Mostra uma lista vazia
pessoa["nome"] = "Leonardo"
pessoa["sobrenome"] = "Conceição"

# Quando a chave não existe gera uma KeyError:
# print(pessoa['nome1'])

# Imprimindo o dicionário
print(pessoa)

# Modificando o valor de uma chave dinamicamente
pessoa["nome"] = "Lúcia"

# Imprimindo
print(pessoa["nome"], pessoa["sobrenome"])

# Apagando uma chave
del pessoa["sobrenome"]
print(pessoa)
##

# O método get para obter uma chave e efetuar um teste.
# Por padrão o método get retornará None.
print(pessoa.get("sobrenome"))

# Contornando a exceção com o método get do dicionário
if pessoa.get("sobrenome") is None:
    print("NÃO EXISTE")
else:
    print(pessoa["sobrenome"])

# Criação de chave dinâmica
chave = "idade"
pessoa[chave] = "15"
print(pessoa[chave])
