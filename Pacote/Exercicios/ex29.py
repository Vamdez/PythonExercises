vel = float(input('Digite sua velocidade atual: '))
if vel > 80:
    print('MULTADO, voce utrapassou o limite de 80km/h')
    multa = (vel-80)*7
    print('Você deve pagar uma multa de R${}'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança')
