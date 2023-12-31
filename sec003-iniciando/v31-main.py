nome = 'Luiz Otávio'
altura = 1.80
peso = 95
imc = peso / altura ** 2

"f-strings"
# Uma das utilidades das f-strings é a possibilidade
# de formatar a saída de um número com casas decimais.
# Observando altura temos: {altura:.2f}
# Indica que depois do ponto teremos duas casas decimais.
# São extremamente úteis para saídas de ponto flutuante.
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Luiz Otávio tem 1.80 de altura,
# pesa 95 quilos e seu IMC é
# 29.320987654320987

# Nota do aluno:
# Para formatar um número em formato brasileiro com f-strings
# # no Python, você pode usar o seguinte código:
