# Valor flutuante com formato de moeda pt-br
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
print(locale.format_string('%.2f', 10.00))

# Valores grandes com e sem separador de milhar
print(locale.format_string('%.2f', 56789.46))
print(locale.format_string('%.2f', 56789.46, True))

# Valor monetário com e sem separador de milhar
# O valor monetário já retorna o símbolo da moeda do país
print(locale.currency(12345.67))

# Com separador de milhar (grouping=True)
print(locale.currency(12345.67, grouping=True))
