def lin(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)


def soma():
    a = int(input('Digite um valor: '))
    b = int(input('Digite um valor: '))
    s = a + b
    print(f'A soma é igual a {s}')


def contador(*num):
    print(num[3])


contador(2, 4, 56, 7, 21, 12, 3)
contador(1, 2, 3, 4, 5)
