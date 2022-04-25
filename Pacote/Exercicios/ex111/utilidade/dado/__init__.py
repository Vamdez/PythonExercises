def validador(msg):
    while True:
        valor = str(input(msg))
        if valor.isalpha() or valor.strip() == '':
            print(f'\33[31mERRO, "{valor}" não é um valor válido\33[m')
        else:
            s = valor.replace(',','.')
            return float(s)