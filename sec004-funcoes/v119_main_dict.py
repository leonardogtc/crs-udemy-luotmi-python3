"""
Dicionários em Python (tipo dict)

Dicionários são estruturas de dados do tipo par de "chave" e "valor".

Chaves podem ser consideradas como o "índice" que vimos na lista e
podem ser de tipos imutáveis, tais como:
- str
- int
- float
- bool
- tuple, etc.

O valor pode ser de qualquer tipo, incluindo outro dicionário.

Usamos as chaves - {} - ou a classe dict para criar dicionários.
- Imutáveis: str, int, float, bool, tuple
- Mutável: dict, list

Exemplo:
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ]
}

É possível criar um dicionário dessa forma:
pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')
"""

pessoa = {
    "nome": "Luiz Otávio",
    "sobrenome": "Miranda",
    "idade": 18,
    "altura": 1.8,
    "endereços": [
        {"rua": "tal tal", "número": 123},
        {"rua": "outra rua", "número": 321},
    ],
}
# Mostra todas as chaves e valores do dicionário
# print(pessoa, type(pessoa))

# Acessa uma chave específica
print(pessoa["nome"])
print(pessoa["sobrenome"])

print()

# Mostra somente as chaves do dicionário
for key in pessoa:
    print(key)

# Mostra chaves e valor das chaves
# for key in pessoa:
#     print(key, pessoa[key])
