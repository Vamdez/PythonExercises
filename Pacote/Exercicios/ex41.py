from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
hoje = date.today().year
idade = hoje - ano
if idade <=9:
    print('Voce tem {} anos, você é \33[34m MIRIM \33[m'.format(idade))
elif idade <= 14:
    print('Voce tem {} anos, voce é \33[34m INFANTIL \33[m'.format(idade))
elif idade <= 19:
    print('Voce tem {} anos, voce é \33[34m JUNIOR \33[m'.format(idade))
elif idade <= 25:
    print('Voce tem {} anos, voce é \33[34m SENIOR \33[m'.format(idade))
else:
    print('Voce tem {} anos, voce é \33[34m MASTER \33[m'.format(idade))