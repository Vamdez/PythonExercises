print('#'*22)
print('Progressão Aritimética')
print('#'*22)
first = int(input('Digite o valor do primeiro termo da PA: '))
razao = int(input('Digite o valor da razao da PA:'))

for c in range(0, 10):
    print(f'{first} -> ', end='')
    first += +razao
print('ACABOU')