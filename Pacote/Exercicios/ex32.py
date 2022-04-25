from datetime import date
ano = int(input('Digite o ano que deseja analisar: , Digite 0 caso queira o ano atual'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{}  é um ano Bissexto'.format(ano))
else:
    print('{} NÃO é um ano Bissexto'.format(ano))

