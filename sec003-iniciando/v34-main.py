# Condicionais mudam o fluxo do código
# if / elif      / else
# se / se não se / se não
entrada = input('Você quer "entrar" ou "sair"? ')

# A instrução if entrada == 'entrar': retornará True
# (verdadeiro) ou False (falso)
# O if pode existir sozinho independente de elif e else.
if entrada == 'entrar':
    # Tem que sempre prestar atenção nos blocos pertencentes
    # a uma sentença. Observe que o comando print('Você entrou no sistema')
    # está recuado em relação a instrução if entrada == 'entrar':. Isto
    # quer dizer que essa instrução pertence ao bloco if
    print('Você entrou no sistema')
    # Pode-se existir diversas instruções dentro de um bloco
    print(12341234)
elif entrada == 'sair':
    print('Você saiu do sistema')

# O else independe de elif mas depende de if. Sempre seguido por
# um sinal de dois pontos (:)
else:
    print('Você não digitou nem entrar e nem sair.')

# Uma instrução fora dos blocos é executada de qualquer maneira
print('FORA DOS BLOCOS')
