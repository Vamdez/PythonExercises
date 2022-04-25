print('-'*40)
print('{: ^40}'.format('SUPERMERCADO'))
print('-'*40)
menor = 0
nmenor = ''
s = 0
count = 0
while True:
    opc = ' '
    name = str(input('Nome do produto: ')).strip().title()
    price = float(input('Preço: R$'))
    if price < menor or menor == 0:     #maisbarato
        menor = price
        nmenor = name
    if price > 1000:        #acimade1000
        count += 1
    s += price              #preçototal
    while opc not in 'SN':
        opc = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if opc == 'N':
        break
print(f'O total da compra foi R${s:.2f}')
print(f'Temos {count} produto custando mais de R$1000')
print(f'O produto mais barato foi {nmenor}, custando R${menor:.2f}')