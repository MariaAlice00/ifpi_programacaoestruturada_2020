conta = float(input('Qual o valor da conta: '))

divisao = conta // 3
resto = conta % 3

print('Carlos: R$ {:.2f}'.format(divisao))
print('André: R$ {:.2f}'.format(divisao))
print('Felipe: R$ {:.2f}'.format(divisao + resto))