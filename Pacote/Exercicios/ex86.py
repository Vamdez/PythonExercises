princ = [[], [], []]
for c in range(3):
    for j in range(3):
        princ[c].append(int(input(f'Digite um valor para [{c}] [{j}]: ')))
print('-='*30)
for x in range(3):
    for y in range(3):
        print(f'[{princ[x][y]:^5}]', end='')
    print('\n')
