"""
Tipo tupla - Uma lista imutável

"""
# A tupla é criada entre parênteses ou não colocando nada para limitar
# ? nomes = ('Leonardo', 'Lúcia', 'Oliver')
# ? nomes = 'Leonardo', 'Lúcia', 'Oliver'
nomes = ('Leonardo', 'Lúcia', 'Oliver')

print(type(nomes))
print(nomes)

# A tupla também responde as mesmas regras de índices da lista
print(nomes[-1])
print(nomes[0])

# Uma tupla pode ser convertida em lista e vice-e-versa
# Convertendo em lista...
# ! NOTA: Mesmo convertendo em lista o comando append e insert foram ignorados.
# nomes = list(nomes)
# nomes.insert(1000, "Ivonete")
# print(type(nomes))

# Convertendo para Tupla
# nomes = tuple(nomes)
