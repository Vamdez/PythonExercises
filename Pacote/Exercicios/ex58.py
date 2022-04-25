from random import randint
tentativas = 1
n1 = randint(0, 10)
print('Sou eu, o Computador!!! \n'
      'Pensei em um número entre \33[34m 0 \33[me\33[34m 10\33[m')
j1 = int(input('Adivinha o número que estou pensando:'))
while j1 != n1:
    if j1 < n1:
        j1 = int(input('Mais...... tente novamente:'))
    else:
        j1 = int(input('Menos....... tente novamente: '))
    tentativas += 1
print(f'Parabens você acertou o número em {tentativas} tentativas')