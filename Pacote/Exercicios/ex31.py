dis = float(input('Qual a distância de sua viagem:'))
if dis <= 200:
    print('Você está prestes a fazer uma viagem de {}'.format(dis))
    total = dis*0.5
    print('E o preço de sua passagem será R${:.2f}'.format(total))
else:
    print('Você está prestes a fazer uma viagem de {}'.format(dis))
    total = dis*0.45
    print('E o preço de sua passagem será R${:.2f}'.format(total))