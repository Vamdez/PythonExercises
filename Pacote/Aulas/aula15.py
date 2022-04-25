cont = s = 0
while True:
    cont = int(input('Digite um numero:'))
    if cont == 999:
        break
    s += cont
print(f'a soma é igual a {s}')

