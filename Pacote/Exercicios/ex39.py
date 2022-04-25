import datetime
ano = datetime.date.today().year
idade = ano - int(input('Digite o ano de seu nascimento:'))
if idade > 18:
    print('Ja passou o ano do seu alistamento')
    print('O seu alistamento foi a {} anos'.format(idade - 18))
elif idade < 18:
    print('O ano do seu alistamento ainda não chegou')
    print('Seu alistamento é daqui a {} anos'.format(18-idade))
else:
    print('Esta no ano do seu alistamento')