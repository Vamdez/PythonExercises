def validador(msg):
    while True:
        valor = str(input(msg))
        if valor.isalpha() or valor.strip() == '':
            print(f'\33[31mERRO, "{valor}" não é um valor válido\33[m')
        else:
            s = valor.replace(',','.')
            return float(s)


def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg).strip())
        except (ValueError, TypeError):
            print('ERRO, Digite um valor válido')
            continue
        return valor


def leiaFloat(msg):
    while True:
        try:
            valor = float(input(msg).strip())
        except (TypeError, ValueError):
            print('ERRO, Digite um valor válido')
            continue
        return valor



