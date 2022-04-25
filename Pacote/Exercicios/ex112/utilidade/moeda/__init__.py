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


def linha(msg):
    print('-'*30)
    print(f'{msg: ^30}')
    print('-'*30)


def resumo(pre, aum, dim):
    linha('RESUMO DO VALOR')
    print(f'{"Preço Analisado: ":<20} {moeda(pre):<8}')
    print(f'{"Dobro do preço: ":<21}{dobro(pre):<8}')
    print(f'{"Metade do preço: ":<20} {metade(pre):<8}')
    print(f'{f"Aumentando {aum}%:":<20} {aumentar(pre, aum):<8}')
    print(f'{f"Diminuindo {dim}%:":<20} {diminuir(pre, dim):<8}')
    print('-' * 30)
