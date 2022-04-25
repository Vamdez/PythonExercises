def aumentar(val, taxa):
    res = val * (1+(taxa/100))
    return moeda(res)


def diminuir(val, taxa):
    res = val * ((100-taxa) / 100)
    return moeda(res)


def metade(val):
    res = val/2
    return moeda(res)


def dobro(val):
    res = val * 2
    return moeda(res)


def moeda(val):
    val = f'{val:.2f}'
    val = str(val)
    return 'R$' + val.replace('.', ',')
