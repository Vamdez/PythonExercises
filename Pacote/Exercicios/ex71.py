import math
print('='*20)
print('{: ^20}'.format('BANCO CENTRAL'))
print('='*20)
n50 = n20 = n10 = n1 = resto = 0
v1 = int(input('Qual valor deseja sacar:'))
n50 = math.trunc(v1/50)
resto = v1 % 50
n20 = math.trunc(resto / 20)
resto = resto % 20
n10 = math.trunc(resto / 10)
resto = resto % 10
n1 = resto
print(f'Total de {n50} cédulas de R$50')
print(f'Total de {n20} cédulas de R$20')
print(f'Total de {n10} cédulas de R$10')
print(f'Total de {n1} cédulas de R$1')