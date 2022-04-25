first_value = int(input('Digite o primeiro valor: '))
pa_ratio = int(input('Digire a razão da PA: '))
cont = 0
total = 0
while cont < 10:
    if cont == 0:
        total = first_value
    else:
        total += pa_ratio
    print(total, end='')
    if cont != 9:
        print(' --> ', end='')
    else:
        print('.')
    cont += 1
