valor = float(input('Digite o valor: '))

entrada = valor // 3
resto = valor % 3
entrada_f = entrada + resto
prestacao = valor - entrada_f
prestacao_f = prestacao /2

from time import sleep

print('******* VALOR DA COMPRA ********')
print('Processando...')
sleep(2)
print('Valor da compra: R$ {:.2f}'.format(valor))
print('Entrada: R$ {:.2f}'.format(entrada_f))
print('Prestações: 2 x de R$ {:.2f}.'.format(prestacao_f))
print('*********************************')