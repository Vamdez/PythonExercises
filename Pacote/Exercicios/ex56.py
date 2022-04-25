l1 = []
total = 0
maior = 0
nomev = ''
cont = 0
for c in range(1, 5):
    print(f'------ {c}ª PESSOA ------')
    nome = str(input('Nome:')).strip().title()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo[M/F]:')).upper().strip()

    if idade > maior and sexo == 'M': #homemmaisvelho
        maior = idade
        nomev = nome

    total += idade
    if sexo == 'F' and idade < 20:
        cont += 1
media = total/4
print(f'A média de idade do grupo é igual a {media} anos')
print(f'O homem mais velho tem {maior} anos, e seu nome é {nomev}')
print(f'Ao todo são {cont} mulheres com menos de 20 anos')
