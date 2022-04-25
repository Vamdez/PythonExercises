princ = [[], []]
for c in range(7):
    v1 = int(input(f'Digite o {c+1}° valor: '))
    if v1 % 2 == 0:
        princ[0].append(v1)
    else:
        princ[1].append(v1)
print(f'Os valores pares digitados foram:{sorted(princ[0])}')
print(f'Os valores impares digitados foram:{sorted(princ[1])}')
