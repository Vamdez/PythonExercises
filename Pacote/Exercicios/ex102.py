def fatorial(num, show=False):
    """
        --> Cacula o Fatorial de um número
    :param num: O numero a ser Calculado
    :param show: (opcional) Mostra ou não a conta
    :return: Retorna o fatorial de num
    """
    fator = 1
    for c in range(num, 0, -1):
        fator = fator*c
        if show == True:
            print(c, end=' ')
            if c != 1:
                print('X', end=' ')
            else:
                print('=', end=' ')
                break
    return fator


print(fatorial(10))
