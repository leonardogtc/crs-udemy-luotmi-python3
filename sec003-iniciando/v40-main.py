# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# * Se qualquer valor for considerado falso,
# * a expressão inteira será avaliada naquele valor

# São considerados falsy:
# 0
# print(bool(0))

# 0.0
# print(bool(0.0))

# ''
# print(bool(''))

# False
# print(bool(False))

# Também existe o tipo None que é
# usado para representar um não valor
# None
# print(bool(None))

# Programa exemplo:
# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if entrada == 'E' and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# Avaliação de curto circuito
print(True and False and True)
print(True and 0 and True)
