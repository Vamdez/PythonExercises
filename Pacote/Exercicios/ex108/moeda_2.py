def aumentar(val, taxa):
    res = val * (1+(taxa/100))
    return  res


def diminuir(val, taxa):
    res = val * ((100-taxa) / 100)
    return res


def metade(val):
    return val/2


def dobro(val):
    return val *2


def moeda(val):
    val = f'{val:.2f}'
    val = str(val)
    return 'R$' + val.replace('.', ',')