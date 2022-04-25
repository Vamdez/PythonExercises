tabela = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians',
          'Red Bull Bragrantino', 'Fluminense','América-MG','Atlético-GO',
          'Santos', 'Ceará', 'Internacional', 'Sao Paulo', 'Athletico-Pr',
          'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')
print('=-=-'*10)
print(f'Lista de classificação de times no brasileirão: {tabela}')
print('=-=-'*10)
print(f'Os 5 primeiros são: {tabela[0:5]}')
print('=-=-'*10)
print(f'Os 4 últimos são: {tabela[-4:]}')
print('=-=-'*10)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('=-=-'*10)
print(f'A chapecoense está na posição {tabela.index("Chapecoense")+1}°')

