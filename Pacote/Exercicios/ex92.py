import datetime
ano = datetime.date.today().year
formulario = dict()
formulario['nome'] = str(input('Nome:'))
nascimento = int(input('Ano de Nascimento:'))
formulario['idade'] = ano - nascimento
formulario['carteira'] = int(input('Número Carteira de Trabalho [0 se não tiver]:'))
if formulario['carteira'] != 0:
    formulario['contratação'] = int(input('Ano de Contratação: '))
    formulario['salario'] = int(input('Sálario:'))
    formulario['aposentadoria'] = (formulario['contratação'] + 35) - nascimento
for k, v in formulario.items():
    print(f'{k} tem o valor {v}')
    