num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro: '))

print('Que operação você deseja realizar?')
operacao = str(input('>>> soma, subtração, multiplicação ou divisão? '))

if operacao == 'soma':
    print('num1 + num2 = {}'.format(num1 + num2))
elif operacao == 'subtração':
    print('num 1 - num2 = {}'.format(num1 - num2))
elif operacao == 'multiplicação':
    print('num1 x num2 = {}'.format(num1 * num2))
elif operacao == 'divisão':
    print('num1 / num2 = {}'.format(num1 / num2))
else:
    print('Operação inválida. Tente novamente!')
