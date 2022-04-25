formulario = {}
formulario['nome']= str(input('Nome: '))
formulario['media']= float(input('Média: '))
if formulario['media'] > 7:
    formulario['resultado']= 'Aprovado'
elif formulario['media'] > 5:
    formulario['resultado']= 'Recuperão'
else:
    formulario['resultado']= 'Reprovado'
print('=-'*30)
for k, v in formulario.items():
    print(f'{k} é igual a {v}')
print('Fim')