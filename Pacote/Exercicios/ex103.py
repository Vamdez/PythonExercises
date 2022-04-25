def ficha(gols, nome='<indefinido>'):
    print(f'Nome = {nome},GOLS = {gols}')


n = str(input('Nome do Jogador:').strip())
g = str(input('Numero de gols:'))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == '':
    ficha(gols=g)
else:
    ficha(g, n)
