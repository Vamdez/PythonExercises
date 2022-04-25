v1 = float(input('Digite o valor das compras: R$'))
opc = int(input('Qual a forma de pagamento?\n'
                '[1] A vista no dinheiro \n'
                '[2] A vista no cartao \n'
                '[3] 2x no cartão \n'
                '[4] 3x ou mais no cartão \n'
                'OPÇÃO:'))
if opc == 1:
    v1 = v1 - (10/100*v1)
    print('Você tem 10% de desconto!!')
elif opc == 2:
    v1 = v1 - (5/100*v1)
    print('Você tem 5% de desconto!!')
elif opc == 3:
    v1 = v1
    print('Você não tem nenhum desconto ou juros!!')
elif opc == 4:
    v1 = v1 + (20/100*v1)
    print('Você tem 20% de juros!!')
else:
    print('Valor invalido')
print('Voce vai pagar R${:.2f}'.format(v1))


