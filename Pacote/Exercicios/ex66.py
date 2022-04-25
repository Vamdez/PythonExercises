v1 = count = s = 0
while True:
    v1 = int(input('Digite um número:'))
    if v1 == 999:
        break
    count += 1
    s += v1
print(f'A soma foi igual a {s} e, foram digitados {count} numeros')