import random
import time
v1 = random.randint(1, 3)
v2 = int(input('Escolha uma das opções:\n'
               '[1]Pedra\n'
               '[2]Papel\n'
               '[3]Tesoura\n'
               'Qual a sua jogada:'))
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!')
print('='*20)
if v1 == 1 and v2 == 2:
    print('Computador jogou Pedra\n'
          'Jogador jogou Papel')
    print('='*20)
    print('Jogador ganhou!!')
elif v1 == 1 and v2 == 3:
    print('Computador jogou Pedra\n'
          'Jogador jogou Tesoura')
    print('=' * 20)
    print('Computador ganhou!!')
elif v1 == 2 and v2 == 1:
    print('Computador jogou Papel\n'
          'Jogador jogou Pedra')
    print('=' * 20)
    print('Computador ganhou!!')
elif v1 == 2 and v2 == 3:
    print('Computador jogou Papel\n'
          'Jogador jogou Tesoura')
    print('=' * 20)
    print('Jogador ganhou!!')
elif v1 == 3 and v2 == 1:
    print('Computador jogou Tesoura\n'
          'Jogador jogou Pedra')
    print('=' * 20)
    print('Jogador ganhou!!')
elif v1 == 3 and v2 == 2:
    print('Computador jogou Tesoura\n'
          'Jogador jogou Papel')
    print('=' * 20)
    print('Computador ganhou!!')
elif v1 == v2:
    print('Tivemos um empate')
    print('=' * 20)
    print('Ninguem ganhou!!')
else:
    print('Valores Invalidos')
    print('='*20)




