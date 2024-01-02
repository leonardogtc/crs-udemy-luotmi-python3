""" Calculadora com while """
while True:

    # A instrução startwith('s') -> Começa com a letra 's'
    # A instrução lower() converte para minúsculo
    # Retorna True caso inicie com 's' ou False caso não
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
