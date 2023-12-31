# if / elif      / else
# se / se não se / se não

condicao1 = True
condicao2 = True
condicao3 = True
condicao4 = True

# O elif permite chegar diversas condições dentro do bloco
# Quando o bloco condicional encontra uma condição verdadeira,
# o fluxo de verificações é interrompido e as instruções
# subsequentes são ignoradas. Por exemplo, se a condição 2
# for verdadeira, as condições 3 e 4 são ignoradas pelo
# sistema efetuando a saída do bloco condicional.
if condicao1:
    print('Código para condição 1')
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição foi satisfeita.')

# Uma instrução if pode existir independente de elif e else
if 10 == 10:
    print('Outro if')

print('Fora do if')
