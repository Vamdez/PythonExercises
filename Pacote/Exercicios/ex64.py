v1 = 0
count = 0
plus = 0
while v1 != 999:
    v1 = int(input('Digite um número [999 pra parar]: '))
    if v1 != 999:
        count += 1
        plus += v1
print(f'The plus is: {plus} and the count is: {count}')
print('FIM')