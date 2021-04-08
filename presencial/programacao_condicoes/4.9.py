valor = float(input('Valor da casa: R$ '))
salario = float(input('Seu salário: R$ '))
anos = float(input('Quantidade de anos: '))

prestacao = valor / (anos * 12)

if prestacao > 0.30 * salario:
    print('O valor do seu salário não permite calcular a prestação.')
else:
    print('A prestação mensal é de: R$ {:.2f}'.format(prestacao))