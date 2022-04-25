extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito',
           'nove', 'dez', 'onze', 'doze', 'treze', 'catorce', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    opc = ' '
    v1 = int(input('Digite um número entre 0 e 20:'))
    if v1 in range(0, 21):
        print(f'Você digitou o número {extenso[v1]}')
        while opc not in 'SN':
            opc = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
            if opc not in 'SN':
                print('Tente Novamente.')
    else:
        print('Tente Novamente.')
    if opc == 'N':
        break

print('Fim')
