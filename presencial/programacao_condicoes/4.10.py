kwh = float(input('Quantidade de kwh consumida: '))
print('Tipo de instalação. Digite, em letra maiúscula por favor:')
print('R - residências')
print('I - indústrias')
print('C - comércios')
tipo = str(input('>>> '))

if tipo == 'R':
    if kwh <= 500:
        print('Preço a pagar: R$ {:.2f}'.format(kwh * 0.40))
    else:
        print('Preço a pagar: R$ {:.2f}'.format(kwh * 0.65))
elif tipo == 'C':
    if kwh <= 1000:
        print('Preço a pagar: R$ {:.2f}'.format(kwh * 0.55))
    else:
        print('Preço a pagar: R$ {:.2f}'.format(kwh * 0.60))
elif tipo == 'I':
    if kwh <= 5000:
        print('Preço a pagar: R$ {:.2f}'.format(kwh * 0.55))
    else:
        print('Preço a pagar: R$ {:.2f}'.format(kwh * 0.60))
else:
    print('Você digitou algo errado!')
