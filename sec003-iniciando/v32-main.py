a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
# Gera um erro: string = 'a = {} b = {} c = {:.2f} {}'
# IndexError: Replacement index 3 out of range for positional args tuple
# indica que foi inserida uma chamada a uma posição inexistente.

string = 'a = {} b = {} c = {:.2f}'

# Fazendo chamada por índices
string = 'a = {0} a = {0} a = {0} b = {1} c = {2:.2f}'

formato = string.format(a, b, c)

# Fazendo chamada por parâmetro nomeado
# Tudo o que vier depois de um parâmetro nomeado tem que ser nomeado também
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'

formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)
