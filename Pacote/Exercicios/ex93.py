jogador = dict()
gols = list()
total = 0
jogador['nome'] = str(input('Nome: ')).title()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(partidas):
    v1 = int(input(f'Quantos gols na {c + 1}° partida:'))
    gols.append(v1)
    total += v1
jogador['gols'] = gols.copy()
jogador['total'] = total
print('-='*30)
print(jogador)
print('-='*30)
for k ,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O Jogador {jogador["nome"]} fez {partidas} partidas')
for c in range(partidas):
    print(f'   => Na {c +1}° partida, fez {jogador["gols"][c]} gols')
print(f'Foi um total de {jogador["total"]} gols')