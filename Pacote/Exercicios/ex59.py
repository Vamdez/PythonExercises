from time import sleep
n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
v = 0

while v != 5:
    print('[1]- Somar os números\n'
          '[2]- Multiplicar os números\n'
          '[3]- Mostrar o maior número\n'
          '[4]- Escolher novos números\n'
          '[5]- Sair do programa')
    v = int(input('>>>>>>>>>Sua opção:'))
    if v == 1:
        t = n1 + n2
        print('A soma é igual a', t)
    elif v == 2:
        t = n1 * n2
        print('A multiplicação é igual a', t)
    elif v == 3:
        if n1 > n2:
            print(f'O número {n1} é maior que o número {n2}')
        elif n1 < n2:
            print(f'O número {n2} é maior que o número {n1}')
        else:
            print('Os valores são iguais')
    elif v == 4:
        n1 = int(input('Digite o 1° número: '))
        n2 = int(input('Digite o 2° número: '))
    else:
        print('Opcão invalída. Tente novamente')
    print('=-'*15)
print('Finalizando.....')
sleep(2)
print('Obrigado por usar nosso serviço :)')
