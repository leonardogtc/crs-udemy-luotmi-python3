"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""

def imprimir(a,b,c):
    print(a,b,c)
    
imprimir(10,20,30)
imprimir(1,2,3)

"""
Com o nome (argumento) igualado a algo, diz que a variável tem um valor padrão
"""
def saudacao(nome='Sem nome'):

    print(f'Olá {nome}!')
    
saudacao('Leonardo')
saudacao()