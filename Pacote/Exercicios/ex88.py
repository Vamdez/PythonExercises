import random
princ = []
temp = []
resultado = []
count = 0
for n in range(7):
    aleatorio = 0
    while aleatorio in temp:
        aleatorio = random.randint(1, 60)
    temp.append(aleatorio)
del(temp[0])
temp.sort()
resultado = temp[:]
temp.clear()
v1 = int(input('Quantos jogos você quer que eu sortei?'))
for c in range(v1):
    for n in range(7):
        aleatorio = 0
        while aleatorio in temp:
            aleatorio = random.randint(1, 60)
        temp.append(aleatorio)
    del(temp[0])
    temp.sort()
    princ.append(temp[:])
    temp.clear()
for c in range(len(princ)):
    if sorted(resultado) == princ[c]:
        print(f'\33[32m{princ[c]}\33[m')
        count += 1
    else:
        print(f'\33[31m{princ[c]}\33[m')
print(f'\33[34m{resultado}\33[m')
print(f'{count} Acertos')


