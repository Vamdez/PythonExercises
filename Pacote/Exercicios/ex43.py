peso = float(input('Digite sua peso(Kg): '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / (altura**2)
if imc < 18.5:
    print('Seu imc é igual a {:.2f},\33[33m voce esta ABAIXO DO PESO\33[m'.format(imc))
elif imc < 25:
    print('Seu imc é igual a {:.2f},\33[32m você está no PESO IDEAL\33[m'.format(imc))
elif imc <30:
    print('Seu imc é igual a {:.2f},\33[93m você está no SOBREPESO\33[m'.format(imc))
elif imc < 40:
    print('Seu imc é igual a {:.2f},\33[33m você está em OBESIDADE\33[m'.format(imc))
else:
    print('Seu imc é igual a {:.2f},\33[31m você está em OBESIDADE MORBITA CUIDADO!!! \33[m'.format(imc))