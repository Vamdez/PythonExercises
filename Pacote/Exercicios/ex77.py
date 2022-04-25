palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for pos in range(len(palavras)):
    count = 0
    print(f'\n{palavras[pos]}', end='')
    while count < len(palavras[pos]):
        if palavras[pos][count] in 'aeiou':
            print(f' -> {palavras[pos][count]}', end='')
        count += 1
print('\nFIM')

