import random
from time import sleep
choice = random.randint(0, 5)
num = int(input('Pense em um número de 0 a 5:'))
print('{}'.format('=-'*20))
print('PROCESSANDO...')
sleep(2)
if num == choice:
    print('acertou')
else :
    print('errou')

print('{}'.format('=-'*20))


