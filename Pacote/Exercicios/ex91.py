from random import randint
from time import sleep
import operator
valores = dict()
for c in range(4):
    v1 = randint(1, 6)
    valores[f'jogador{c+1}'] = v1
print('Valores Sorteados')
for k, v in valores.items():
    print(f'{k} tirou {v} no dado')
    sleep(0.5)
print('='*30)
print('==Rank dos jogadores==')
ranked = list()
ranked = sorted(valores.items(), key=operator.itemgetter(1), reverse=True)
for i, v in enumerate(ranked):
    print(f'{i+1}° foi o {v[0]} com {v[1]}')
    sleep(0.5)