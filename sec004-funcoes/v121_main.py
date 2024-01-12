"""
Métodos úteis dos dicionários em Python
    len - quantas chaves
    keys - iterável com as chaves
    values - iterável com os valores
    items - iterável com chaves e valores
    setdefault - adiciona valor se a chave não existe
    copy - retorna uma cópia rasa (shallow copy)
    get - obtém uma chave
    pop - Apaga um item com a chave especificada (del)
    popitem - Apaga o último item adicionado
    update - Atualiza um dicionário com outro
"""
pessoa = {
    "nome": "Leonardo",
    "sobrenome": "Conceição",
    "idade": 900,
}

# setdefault - adiciona valor se a chave não existe
# Caso a indade não exista no dicionário ele retorna
# o valor padrão 0
pessoa.setdefault("idade", 0)
print(pessoa["idade"])

# Retorna o número de chaves no dicionário
print(len(pessoa))

# Retorna um dicionário de chaves
print(pessoa.keys())
print(list(pessoa.keys()))
print(list(pessoa.values()))
print(list(pessoa.items()))

# Pega os valores do dicionário
for valor in pessoa.values():
    print(valor)

# Através dos items() pega chave e valor
for chave, valor in pessoa.items():
    print(chave, ":", valor)
