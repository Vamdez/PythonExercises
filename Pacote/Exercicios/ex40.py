num1 = float(input('Digite sua primeira nota:'))
num2 = float(input('Digite sua segunda nota'))
media = (num1+num2)/2
print('SUA MEDIA FOI {}'.format(media))
if media < 5:
    print('REPROVADO')
elif media >= 7:
    print('APROVADO')
else:
    print('RECUPERAÇAO')