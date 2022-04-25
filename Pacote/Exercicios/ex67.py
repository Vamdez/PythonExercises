v1 = 0
while True:
    v1 = int(input('Deseja ver a tabuada de que valor: '))
    count = 0
    print('-' * 20)
    if v1 < 0:
        break
    while count < 10:
        count +=1
        print(f'{v1} x {count} = {v1*count}')
    print('-'*20)
print('Fim do programa')