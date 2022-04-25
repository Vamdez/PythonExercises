sex = str(input('Informe seu sexo [F/M]:')).upper().strip()
while sex not in 'MF':
    sex =str(input('Dados invalidos, digite seu sexo [F/M]')).strip().upper()
print(f'Sexo {sex} registrado com sucesso')
