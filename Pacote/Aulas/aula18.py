teste = list()
teste.append('Victor')
teste.append(18)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 39
galera.append(teste[:])
print(galera)
