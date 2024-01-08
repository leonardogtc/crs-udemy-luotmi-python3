"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

# Definindo x externamento, o x deve ser definido
# antes de chamar a função
x = 1


def escopo():
    # A variável está definida no escopo da função
    # só pode ser acessado chamando a função.
    # x = 1
    # Uma variável no escopo da função ter a
    # preferência da função
    global x
    x = 10
    def outra_funcao():
        global x
        x = 11
        y = 2
        print(x, y)
        
    outra_funcao()
    print(x)

print(x)
escopo()
print(x)
