print('-='*20)
print(' '*8, '\33[34m Sequencia Fibonacci\33[m')
print('-='*20)
termos = int(input('Quantos termos deseja mostrar:'))
v1 = 0
v2 = 1
total = 0
print(f'{v1} --> {v2}', end='')
while termos > 0:
    total = v1 + v2
    v1 = v2
    v2 = total
    print(f' --> {total}', end='')
    termos -= 1
print(' --> Fim')