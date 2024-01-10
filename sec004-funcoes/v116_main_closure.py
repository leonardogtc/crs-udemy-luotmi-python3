'''
Closure e funções que retornam outras funções
Uma função que cria outra função.
'''


def criar_saudacao(saudacao):
    """_Cria uma saudação_

    Args:
        saudacao (_string_): _Um text para saudar uma pessoa_
    """
    def saudar(nome):
        return f"{saudacao}, {nome}!"

    # O retorno da função "saudar" sem os parênteses diz a função
    # que esta armazenará na memória a função para fazer posteriormente
    # a chamada pedindo o nome.
    return saudar


# Armazena a função criar_saudacao dentro da variável
# falar_bom_dia - Isto que dizer em outras palavras que
# falar_bom_dia armazenou o primeiro resultado, recebendo
# bom dia e adiou a recepção do nome da função saudar.
falar_bom_dia = criar_saudacao("Bom dia")
falar_boa_noite = criar_saudacao("Boa noite")

# A cada passagem de for realiza a iteração com a lista de nomes
for nomes in ["Maria", "Joana", "Luiz"]:
    # O print chama "falar_bom_dia" e "falar boa noite" como uma
    # função passando o parâmetro nome, pois o parâmetro saudação
    # foi passado anteriormente. (Isto é o closer - fechamento)
    print(falar_bom_dia(nomes))
    print(falar_boa_noite(nomes))
