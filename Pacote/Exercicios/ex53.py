frase = str(input('Digite uma frase:')).upper().replace(' ', '')
nletras = len(frase)
s = ""
for c in range(nletras, 0, -1):
    s = s + frase[c - 1]
print(f'O inverso de {frase} é {s}')
if s == frase:
    print('Temos um palindromo!!')
else:
    print('Não temos um palindromo!!')





