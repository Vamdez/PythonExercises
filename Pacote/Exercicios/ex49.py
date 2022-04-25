v1 = int(input('Digite o numero da tabuada que deseja: '))
for c in range(1, 11):
    res = c * v1
    print('{} x {} = {}'.format(v1, c, res))
