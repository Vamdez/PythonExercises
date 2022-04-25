pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': '19'}
del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')
