"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada
está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
"""
import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0
numero_tentativas_erradas = 0

while True:

    letra_digitada = input("Digite uma letra: ")
    numero_tentativas += 1

    if letra_digitada == 0:
        break

    if len(letra_digitada) > 1:
        print('Digite somente uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    else:
        numero_tentativas_erradas += 1

    palavra_formada = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada: ', palavra_formada)

    # Venceu
    if palavra_secreta == palavra_formada:
        # Limpar o terminal no Linux
        os.system('clear')

        # Mensagens do vencedor
        print('VOCÊ GANHOU! PARABÉNS!')
        print('A palavra secreta era ', palavra_secreta)
        print('Tentativas: ', numero_tentativas)
        print('Erros: ', numero_tentativas_erradas)

        # reiniciando variáveis
        letras_acertadas = ''
        numero_tentativas = 0
        numero_tentativas_erradas = 0
