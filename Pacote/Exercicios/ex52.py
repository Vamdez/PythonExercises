v1 = int(input('Digite um número: '))
n = 0
for c in range(1, v1+1):
    if v1 % c == 0:
        print(f'\33[92m {c} \33[m', end='')
        n += + 1
    else:
        print(f'\33[91m {c} \33[m', end='')
print(f'\nO numero {v1} é divisivel {n} vezes')
if n > 2:
    print('E por isso NÃO é um número PRIMO')
else:
    print('E por isso é um número PRIMO')
