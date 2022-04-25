print('PROGRESSAO ARITIMETICA')
print('-'*34)
first_value = int(input('Primeiro termo:'))
pa_ratio = int(input('Razao da PA: '))
value = 10
cont = 0
while value > 0:
    if cont == 0:
        print(first_value, '--> ', end='')
    else:
        first_value += pa_ratio
        print(first_value, '--> ', end='')
    value -= 1
    cont += 1
    if value == 0:
        print('PAUSE')
        value = int(input('Quantos termos pretende adicionar a mais: '))
print(f'Progressão finalizada com {cont} termos')