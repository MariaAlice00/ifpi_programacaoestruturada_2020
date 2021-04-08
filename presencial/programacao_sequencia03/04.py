valor = int(input('Digite o valor: '))

cinquenta = valor // 50
resto = valor % 50
dez = resto // 10
resto = resto % 10
cinco = resto // 5
resto = resto % 5
dois = resto // 2

from time import sleep

print('******* VOCÊ IRÁ SACAR *******')
print('Processando...')
sleep(2)
print('>>> {} nota(s) de R$ 50'.format(cinquenta))
print('>>> {} notas(s) de R$ 10'.format(dez))
print('>>> {} notas(s) de R$ 5'.format(cinco))
print('>>> {} notas(s) de R$ 2'.format(dois))
print('*******************************')