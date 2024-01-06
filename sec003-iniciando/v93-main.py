"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""

# Separa a frase pelos espaços em branco
frase = 'Olha só que, coisa interessante'
lista_frase = frase.split()
# ? print(lista_frase)

# Separa por um caractere (vírgula)
lista_frase = frase.split(',')
# ? print(lista_frase)

# Descarta os espaços no início e no fim palavra
frase = '   Olha só que   , coisa interessante          '
lista_frase = frase.split()
# ? print(lista_frase)

# Corrige os espaços na lista
lista_frases_cruas = frase.split(',')
lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

print(lista_frases_cruas)
print(lista_frases)

# Unindo a lista em um texto
frases_unidas = ', '.join(lista_frases)
print(frases_unidas)
