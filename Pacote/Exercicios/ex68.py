from random import randint
count = 0
print('=-'*20)
print('VAMOS JOGAR PAR OU IMPAR')
while True:
    print('=-' * 20)
    computador = randint(0, 9)
    v1 = int(input('Diga um valor:'))
    opc = str(input('Par ou Impar[P/I]')).strip().upper()
    print('=-'*20)
    teste = (v1 + computador) % 2
    if teste == 0:
        print(f'Você jogou {v1} e o computador {computador}. Total {v1 + computador} DEU PAR')
        if opc == 'P':
            print('Você venceu!\nVamos jogar novamente...')
        else:
            print(f'GAME OVER! Você venceu {count} vezes.')
            break
    elif teste == 1:
        print(f'Você jogou {v1} e o computador {computador}. Total {v1 + computador} DEU IMPAR')
        if opc == 'I':
            print('Você venceu! \nVamos jogar novamente...')
        else:
            print(f'GAME OVER! Você venceu {count} vezes.')
            break
    count += 1

