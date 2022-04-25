time = list()
jogador = dict()
gols = list()
while True:
    total = 0
    opc = ' '
    jogador['nome'] = str(input('Nome: ')).title()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(partidas):
        v1 = int(input(f'Quantos gols na {c + 1}° partida:'))
        gols.append(v1)
        total += v1
    jogador['gols'] = gols.copy()
    jogador['total'] = total
    time.append(jogador.copy())
    jogador.clear()
    gols.clear()
    while opc not in 'SN':
        opc = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if opc == 'N':
        break
print('-='*30)

print(f'opc nome        gols        total')
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:<2}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    while True:
        resp = int(input('Deseja saber informações de qual jogador?[999 pra parar]'))
        if resp in range(len(time)) or resp == 999:
            break
        print('Valor invalído')
    if resp == 999:
        break
    print(f'Levantamento do jogador {time[resp]["nome"]}')
    for c in range(len(time[resp]['gols'])):
        print(f'    No jogo {c+1} fez {time[resp]["gols"][c]} gols')
    print('-'*40)
print('OBRIGADO POR USAR NOSSO SERVIÇO')

