def leiaInt(msg):
    while True:
        n = str(input(msg).strip())
        if n.isnumeric():
            return n
        else:
            print('\33[31mO valor digitado não é um número inteiro\33[m')


n = leiaInt('Digite um número: ')
print(f'{n} é um número')