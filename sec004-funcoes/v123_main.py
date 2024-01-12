# Métodos úteis dos dicionários em Python
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
p1 = {
    "nome": "Luiz",
    "sobrenome": "Miranda",
}

print(p1["nome"])
print(p1.get("nome", "Não existe"))

# pop - Apaga um item com a chave especificada (del) mas retornando seu valor
# nome = p1.pop('nome')
# print(nome)
# print(p1)

# popitem - Apaga o último item adicionado
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)

# update - Atualiza um dicionário com outro
# p1.update({
#     'nome': 'novo valor',
#     'idade': 30,
# })

# Outra forma do update
# p1.update(nome="novo valor", idade=30)

# Update por tupla
# tupla = (('nome', 'novo valor'), ('idade', 30))
# p1.update(tupla)

# update por lista
lista = [["nome", "novo valor"], ["idade", 52]]
p1.update(lista)

print(p1)
